import requests
import time
import threading
import queue

class Api42():
    def __init__(self, client_id, client_secret, scope, threads=1, threading=False):
        self.client_id = client_id
        self.client_secret = client_secret
        self.scope = scope
        self.api_url = 'https://api.intra.42.fr/v2'
        self.session = requests.Session()
        self.session.headers.update(self.__getTokenHeader())
        self.threads = threads
        self.threading = threading
        
    def __combine_dict(self, args):
        d = {}
        for arg in args:
            d.update(arg)
        return d
    
    def __getTokenHeader(self):
        config = {
            'grant_type' : 'client_credentials',
            'client_id' : self.client_id,
            'client_secret' : self.client_secret,
            'scope' : self.scope
        }
        r = requests.post(f'{self.api_url}/oauth/token', config)
        if r.status_code != 200:
            raise Exception("Error: " + str(r.status_code) + " " + r.text)
        token =  { 'Authorization': 'Bearer ' + r.json()['access_token']  }
        return token
    
    def __multiThreadingGetPage(self, url, params, page, _queue):
        params.update({'per_page': 100, 'page': page})
        r = self.session.get(f'{self.api_url}{url}', params=params)
        if r.status_code == 401 and r.json()['message'] == "The access token expired":
            self.session.headers.update(self.__getTokenHeader())
            return self.__multiThreadingGetPage(url, params, page, _queue)
        elif r.status_code == 429:
            time.sleep(0.5)
            return self.__multiThreadingGetPage(url, params, page, _queue)
        elif r.status_code != 200:
            raise Exception("Error: " + str(r.status_code) + " " + r.text)
        res = r.json()
        _queue.put(res)
        
    def __multiThreadedPaginatedData(self, url, params):
        data = []
        Page = 1
        while True:
            queues = [queue.Queue() for i in range(self.threads)]
            threads = []
            new_data = []
            for i in range(self.threads):
                t = threading.Thread(target=self.__multiThreadingGetPage, args=(url, params, Page, queues[i]))
                threads.append(t)
                Page += 1
            for i in range(self.threads):
                threads[i].start()
                time.sleep(0.1)
            for i in range(self.threads):
                threads[i].join()
                new_data += queues[i].get()
            if len(new_data) == 0:
                break
            data += new_data
        return data
    
    def __getPaginatedData(self, url, params):
        if self.threading:
            return self.__multiThreadedPaginatedData(url, params)
        else:
            data = []
            Page = 1
            while True:
                params.update({'per_page': 100, 'page': Page})
                r = self.session.get(f'{self.api_url}{url}', params=params)
                if r.status_code == 401 and r.json()['message'] == "The access token expired":
                    self.session.headers.update(self.__getTokenHeader())
                    return self.__getPaginatedData(url, params)
                elif r.status_code == 429:
                    time.sleep(0.5)
                    return self.__getPaginatedData(url, params)
                elif r.status_code != 200:
                    raise Exception("Error: " + str(r.status_code) + " " + r.text)
                res = r.json()
                if len(res) == 0:
                    break
                data += res
                Page += 1
            return data
        
     
    def __getNonPaginatedData(self, url):
        r = self.session.get(f'{self.api_url}{url}')
        if r.status_code == 401 and r.json()['message'] == "The access token expired":
            self.session.headers.update(self.__getTokenHeader())
            return self.__getNonPaginatedData(url)
        elif r.status_code == 429:
            time.sleep(0.5)
            return self.__getNonPaginatedData(url)
        elif r.status_code != 200:
            raise Exception("Error: " + str(r.status_code) + " " + r.text)
        return r.json()
    
    
    def close(self):
        self.session.close()


    
    # ------------------- GET TOKEN ------------------- #
    
    def getToken(self):
        return self.__getTokenHeader()['Authorization'].split(' ')[1]

    
    # ------------------- Accreditations ------------------- #
    
    def getAllAccreditations(self, *args):
        return self.__getPaginatedData(f'/accreditations/', self.__combine_dict(args))
    
    def getAccreditationByID(self, accreditationId):
        return self.__getNonPaginatedData(f'/accreditations/{accreditationId}')
    
    # ------------------- Achievements ------------------- #
    
    def getAllAchievements(self, *args):
        return self.__getPaginatedData(f'/achievements/', self.__combine_dict(args))
    
    def getAchievementByID(self, achievementId):
        return self.__getNonPaginatedData(f'/achievements/{achievementId}')
    
    def getCursusAchievements(self, cursusId, *args):
        return self.__getPaginatedData(f'/cursus/{cursusId}/achievements/', self.__combine_dict(args))
    
    def getCampusAchievements(self, campusId, *args):
        return self.__getPaginatedData(f'/campus/{campusId}/achievements/', self.__combine_dict(args))
    
    def getTitlesAchievements(self, titleId, *args):
        return self.__getPaginatedData(f'/titles/{titleId}/achievements/', self.__combine_dict(args))
    
    # ------------------- Achievements users ------------------- #
    
    def getAllAchievementsUsers(self, *args):
        return self.__getPaginatedData(f'/achievements_users/', self.__combine_dict(args))
    
    def getAchievementsUsersByID(self, achievementUserId):
        return self.__getNonPaginatedData(f'/achievements_users/{achievementUserId}')
    
    # ------------------- Amendments ------------------- #
    
    def getAllAmendments(self, *args):
        return self.__getPaginatedData(f'/amendments/', self.__combine_dict(args))
    
    def getAmendmentByID(self, amendmentId):
        return self.__getNonPaginatedData(f'/amendments/{amendmentId}')
    
    def getUserAmendments(self, userId, *args):
        return self.__getPaginatedData(f'/users/{userId}/amendments/', self.__combine_dict(args))
    
    def getIntershipsAmendments(self, intershipId, *args):
        return self.__getPaginatedData(f'/interships/{intershipId}/amendments/', self.__combine_dict(args))
    
    # ------------------- Announcements ------------------- #
    
    def getAllAnnouncements(self, *args):
        return self.__getPaginatedData(f'/announcements/', self.__combine_dict(args))
    
    def getAnnouncementByID(self, announcementId):
        return self.__getNonPaginatedData(f'/announcements/{announcementId}')
    
    # ------------------- Anti Grav Units ------------------- #
    
    def getAllAntiGravUnits(self, *args):
        return self.__getPaginatedData(f'/anti_grav_units/', self.__combine_dict(args))
    
    def getAntiGravUnitByID(self, antiGravUnitId):
        return self.__getNonPaginatedData(f'/anti_grav_units/{antiGravUnitId}')
    
    # ------------------- Anti Grav Units Users ------------------- #
    
    def getAllAntiGravUnitsUsers(self, *args):
        return self.__getPaginatedData(f'/anti_grav_units_users/', self.__combine_dict(args))
    
    def getAntiGravUnitsUsersByID(self, antiGravUnitsUserId):
        return self.__getNonPaginatedData(f'/anti_grav_units_users/{antiGravUnitsUserId}')
    
    def getUserAntiGravUnits(self, userId, *args):
        return self.__getPaginatedData(f'/users/{userId}/anti_grav_units/', self.__combine_dict(args))
    
    def getCampusAntiGravUnits(self, campusId, *args):
        return self.__getPaginatedData(f'/campus/{campusId}/anti_grav_units/', self.__combine_dict(args))
    
    # ------------------- Apps ------------------- #
    
    def getAllApps(self, *args):
        return self.__getPaginatedData(f'/apps/', self.__combine_dict(args))
    
    def getAppByID(self, appId):
        return self.__getNonPaginatedData(f'/apps/{appId}')
    
    def getUserApps(self, userId, *args):
        return self.__getPaginatedData(f'/users/{userId}/apps/', self.__combine_dict(args))
    
    # ------------------- Attachments ------------------- #
    
    def getAllAttachments(self, *args):
        return self.__getPaginatedData(f'/attachments/', self.__combine_dict(args))
    
    def getAttachmentByID(self, attachmentId):
        return self.__getNonPaginatedData(f'/attachments/{attachmentId}')
    
    def getProjectSessionsAttachments(self, projectSessionId, *args):
        return self.__getPaginatedData(f'/project_sessions/{projectSessionId}/attachments/', self.__combine_dict(args))
    
    def getProjectAttachments(self, projectId, *args):
        return self.__getPaginatedData(f'/projects/{projectId}/attachments/', self.__combine_dict(args))

    # ------------------- Balances ------------------- #
    
    def getAllBalances(self, *args):
        return self.__getPaginatedData(f'/balances/', self.__combine_dict(args))
    
    def getBalanceByID(self, balanceId):
        return self.__getNonPaginatedData(f'/balances/{balanceId}')
    
    def getPoolsBalances(self, poolId, *args):
        return self.__getPaginatedData(f'/pools/{poolId}/balances/', self.__combine_dict(args))
    
    # ------------------- Bloc deadlines ------------------- #
    
    def getAllBlocDeadlines(self, *args):
        return self.__getPaginatedData(f'/bloc_deadlines/', self.__combine_dict(args))
    
    def getBlocDeadlineByID(self, blocDeadlineId):
        return self.__getNonPaginatedData(f'/bloc_deadlines/{blocDeadlineId}')
    
    def getBlocsBlocDeadlines(self, blocId, *args):
        return self.__getPaginatedData(f'/blocs/{blocId}/bloc_deadlines/', self.__combine_dict(args))
    
    # ------------------- Blocs ------------------- #
    
    def getAllBlocs(self, *args):
        return self.__getPaginatedData(f'/blocs/', self.__combine_dict(args))
    
    def getBlocByID(self, blocId):
        return self.__getNonPaginatedData(f'/blocs/{blocId}')
    
    # ------------------- Broadcasts ------------------- #
    
    def getCampusBroadcasts(self, campusId, *args):
        return self.__getPaginatedData(f'/campus/{campusId}/broadcasts/', self.__combine_dict(args))
    
    # ------------------- campus ------------------- #
    
    def getAllCampuses(self, *args):
        return self.__getPaginatedData(f'/campus/', self.__combine_dict(args))
    
    def getCampusByID(self, campusId):
        return self.__getNonPaginatedData(f'/campus/{campusId}')
    
    def getCampusStats(self, campusId, *args):
        return self.__getPaginatedData(f'/campus/{campusId}/stats/', self.__combine_dict(args))
    
    # ------------------- Certificates ------------------- #
    
    def getAllCertificates(self, *args):
        return self.__getPaginatedData(f'/certificates/', self.__combine_dict(args))
    
    def getCertificateByID(self, certificateId):
        return self.__getNonPaginatedData(f'/certificates/{certificateId}')
    
    # ------------------- Certificates Users ------------------- #
    
    def getAllCertificatesUsers(self, *args):
        return self.__getPaginatedData(f'/certificates_users/', self.__combine_dict(args))
    
    def getCertificateUserByID(self, certificateUserId):
        return self.__getNonPaginatedData(f'/certificates_users/{certificateUserId}')
    
    def getUserCertificates(self, userId, *args):
        return self.__getPaginatedData(f'/users/{userId}/certificates/', self.__combine_dict(args))
    
    def getCertificateCertificatesUsers(self, certificateId, *args):
        return self.__getPaginatedData(f'/certificates/{certificateId}/certificates_users', self.__combine_dict(args))
    
    # ------------------- Closes ------------------- #
    
    def getAllCloses(self, *args):
        return self.__getPaginatedData(f'/closes/', self.__combine_dict(args))
    
    def getCloseByID(self, closeId):
        return self.__getNonPaginatedData(f'/closes/{closeId}')
    
    def getUserCloses(self, userId, *args):
        return self.__getPaginatedData(f'/users/{userId}/closes/', self.__combine_dict(args))
    
    # ------------------- Coalitions ------------------- #
    
    def getAllCoalitions(self, *args):
        return self.__getPaginatedData(f'/coalitions/', self.__combine_dict(args))
    
    def getCoalitionByID(self, coalitionId):
        return self.__getNonPaginatedData(f'/coalitions/{coalitionId}')
    
    def getUserCoalitions(self, userId, *args):
        return self.__getPaginatedData(f'/users/{userId}/coalitions/', self.__combine_dict(args))
    
    def getBlocsCoalitions(self, blocId, *args):
        return self.__getPaginatedData(f'/blocs/{blocId}/coalitions/', self.__combine_dict(args))
    
    # ------------------- Coalitions Users ------------------- #
    
    def getAllCoalitionsUsers(self, *args):
        return self.__getPaginatedData(f'/coalitions_users/', self.__combine_dict(args))
    
    def getCoalitionUserByID(self, coalitionUserId):
        return self.__getNonPaginatedData(f'/coalitions_users/{coalitionUserId}')
    
    def getUserCoalitionsUsers(self, userId, *args):
        return self.__getPaginatedData(f'/users/{userId}/coalitions_users/', self.__combine_dict(args))
    
    def getCoalitionCoalitionsUsers(self, coalitionId, *args):
        return self.__getPaginatedData(f'/coalitions/{coalitionId}/coalitions_users/', self.__combine_dict(args))
    
    # ------------------- Commands ------------------- #
    
    def getProductsCommands(self, productId, *args):
        return self.__getPaginatedData(f'/products/{productId}/commands/', self.__combine_dict(args))
    
    # ------------------- Community Services ------------------- #
    
    def getAllCommunityServices(self, *args):
        return self.__getPaginatedData(f'/community_services/', self.__combine_dict(args))
    
    def getCommunityServiceByID(self, communityServiceId):
        return self.__getNonPaginatedData(f'/community_services/{communityServiceId}')
    
    def getCloseCommunityServices(self, closeId, *args):
        return self.__getPaginatedData(f'/closes/{closeId}/community_services/', self.__combine_dict(args))
    
    # ------------------- Companies ------------------- #
    
    def getAllCompanies(self, *args):
        return self.__getPaginatedData(f'/companies/', self.__combine_dict(args))
    
    def getCompanyByID(self, companyId):
        return self.__getNonPaginatedData(f'/companies/{companyId}')
    
    def getCompanySubscribedUsers(self, companyId, *args):
        return self.__getPaginatedData(f'/companies/{companyId}/subscribed_users/', self.__combine_dict(args))
    
    def getCompanyInternshipsUsers(self, companyId, *args):
        return self.__getPaginatedData(f'/companies/{companyId}/internships_users/', self.__combine_dict(args))
    
    # ------------------- Correction point historics ------------------- #
    
    def GetUserCorrectionPointHistorics(self, userId, *args):
        return self.__getPaginatedData(f'/users/{userId}/correction_point_historics/', self.__combine_dict(args))
    
    # ------------------- Cursus ------------------- #
    
    def getAllCursus(self, *args):
        return self.__getPaginatedData(f'/cursus/', self.__combine_dict(args))
    
    def getCursusByID(self, cursusId):
        return self.__getNonPaginatedData(f'/cursus/{cursusId}')
    
    # ------------------- Cursus Users ------------------- #
    
    def getAllCursusUsers(self, *args):
        return self.__getPaginatedData(f'/cursus_users/', self.__combine_dict(args))
    
    def getCursusUserByID(self, cursusUserId):
        return self.__getNonPaginatedData(f'/cursus_users/{cursusUserId}')
    
    def getCursusCursusUsers(self, cursusId, *args):
        return self.__getPaginatedData(f'/cursus/{cursusId}/cursus_users/', self.__combine_dict(args))
    
    def getUserCursusUsers(self, userId, *args):
        return self.__getPaginatedData(f'/users/{userId}/cursus_users/', self.__combine_dict(args))
    
    # ------------------- Dashes ------------------- #
    
    def getAllDashes(self, *args):
        return self.__getPaginatedData(f'/dashes/', self.__combine_dict(args))
    
    def getDashByID(self, dashId):
        return self.__getNonPaginatedData(f'/dashes/{dashId}')
    
    # ------------------- Dashes Users ------------------- #
    
    def getAllDashesUsers(self, *args):
        return self.__getPaginatedData(f'/dashes_users/', self.__combine_dict(args))
    
    def getDashesUserByID(self, dashUserId):
        return self.__getNonPaginatedData(f'/dashes_users/{dashUserId}')
    
    def getDashesDashesUsers(self, dashId, *args):
        return self.__getPaginatedData(f'/dashes/{dashId}/dashes_users/', self.__combine_dict(args))
    
    # ------------------- Endpoints ------------------- #
    
    def getAllEndpoints(self, *args):
        return self.__getPaginatedData(f'/endpoints/', self.__combine_dict(args))
    
    def getEndpointByID(self, endpointId):
        return self.__getNonPaginatedData(f'/endpoints/{endpointId}')
    
    # ------------------- Evaluations ------------------- #
    
    def getAllEvaluations(self, *args):
        return self.__getPaginatedData(f'/evaluations/', self.__combine_dict(args))
    
    def getEvaluationByID(self, evaluationId):
        return self.__getNonPaginatedData(f'/evaluations/{evaluationId}')
    
    # ------------------- Events ------------------- #
    
    def getAllEvents(self, *args):
        return self.__getPaginatedData(f'/events/', self.__combine_dict(args))
    
    def getEventByID(self, eventId):
        return self.__getNonPaginatedData(f'/events/{eventId}')
    
    def getCursusEvents(self, cursusId, *args):
        return self.__getPaginatedData(f'/cursus/{cursusId}/events/', self.__combine_dict(args))
    
    def getCampusEvents(self, campusId, *args):
        return self.__getPaginatedData(f'/campus/{campusId}/events/', self.__combine_dict(args))
    
    def getUsersEvents(self, userId, *args):
        return self.__getPaginatedData(f'/users/{userId}/events/', self.__combine_dict(args))
    
    # ------------------- Events Users ------------------- #
    
    def getAllEventsUsers(self, *args):
        return self.__getPaginatedData(f'/events_users/', self.__combine_dict(args))
    
    def getEventsUserByID(self, eventsUserId):
        return self.__getNonPaginatedData(f'/events_users/{eventsUserId}')

    def getUsersEventsUsers(self, userId, *args):
        return self.__getPaginatedData(f'/users/{userId}/events_users/', self.__combine_dict(args))
    
    def getEventsEventsUsers(self, eventId, *args):
        return self.__getPaginatedData(f'/events/{eventId}/events_users/', self.__combine_dict(args))
    
    # ------------------- Exams ------------------- #

    def getAllExams(self, *args):
        return self.__getPaginatedData(f'/exams/', self.__combine_dict(args))
    
    def getExamByID(self, examId):
        return self.__getNonPaginatedData(f'/exams/{examId}')
    
    def getCursusExams(self, cursusId, *args):
        return self.__getPaginatedData(f'/cursus/{cursusId}/exams/', self.__combine_dict(args))
    
    def getCampusExams(self, campusId, *args):
        return self.__getPaginatedData(f'/campus/{campusId}/exams/', self.__combine_dict(args))
    
    def getCampusCursusExams(self, campusId, cursusId, *args):
        return self.__getPaginatedData(f'/campus/{campusId}/cursus/{cursusId}/exams/', self.__combine_dict(args))
    
    def getUserExams(self, userId, *args):
        return self.__getPaginatedData(f'/users/{userId}/exams/', self.__combine_dict(args))
    
    def getProjectExams(self, projectId, *args):
        return self.__getPaginatedData(f'/projects/{projectId}/exams/', self.__combine_dict(args))

    # ------------------- Exams Users ------------------- #

    def getExamExamsUsers(self, examId, *args):
        return self.__getPaginatedData(f'/exams/{examId}/exams_users/', self.__combine_dict(args))
    
    # ------------------- Experiences ------------------- #
    
    def getAllExperiences(self, *args):
        return self.__getPaginatedData(f'/experiences/', self.__combine_dict(args))
    
    def getCampusExperiences(self, campusId, *args):
        return self.__getPaginatedData(f'/campus/{campusId}/experiences/', self.__combine_dict(args))
    
    def getProjectUserExperiences(self, projectUserId, *args):
        return self.__getPaginatedData(f'/projects_users/{projectUserId}/experiences/', self.__combine_dict(args))
    
    def getUserExperiences(self, userId, *args):
        return self.__getPaginatedData(f'/users/{userId}/experience/', self.__combine_dict(args))
    
    def getSkillExperiences(self, skillId, *args):
        return self.__getPaginatedData(f'/skills/{skillId}/experiences/', self.__combine_dict(args))

    def getPartnershipUserExperiences(self, partnershipUserId, *args):
        return self.__getPaginatedData(f'/partnerships_users/{partnershipUserId}/experiences/', self.__combine_dict(args))
    
    def getExperienceByID(self, experienceId):
        return self.__getNonPaginatedData(f'/experiences/{experienceId}')
    

    # ------------------- Expertises ------------------- #

    def getAllExpertises(self, *args):
        return self.__getPaginatedData(f'/expertises/', self.__combine_dict(args))
    
    def getExpertiseByID(self, expertiseId):
        return self.__getNonPaginatedData(f'/expertises/{expertiseId}')
    
    # ------------------- Expertises Users ------------------- #

    def getExpertiseExpertisesUsers(self, expertiseId, *args):
        return self.__getPaginatedData(f'/expertises/{expertiseId}/expertises_users/', self.__combine_dict(args))
    
    def getUserExpertisesUsers(self, userId, *args):
        return self.__getPaginatedData(f'/users/{userId}/expertises_users/', self.__combine_dict(args))
    
    def getAllExpertisesUsers(self, *args):
        return self.__getPaginatedData(f'/expertises_users/', self.__combine_dict(args))
    
    def getExpertiseUserByID(self, expertiseUserId):
        return self.__getNonPaginatedData(f'/expertises_users/{expertiseUserId}')
    
    # ------------------- Feedbacks ------------------- #

    def getEventFeedbacks(self, eventId, *args):
        return self.__getPaginatedData(f'/events/{eventId}/feedbacks/', self.__combine_dict(args))
    
    def getAllFeedbacks(self, *args):
        return self.__getPaginatedData(f'/feedbacks/', self.__combine_dict(args))
    
    def getScaleTeamFeedbacks(self, scaleTeamId, *args):
        return self.__getPaginatedData(f'/scale_teams/{scaleTeamId}/feedbacks/', self.__combine_dict(args))
    
    def getEventFeedback(self, eventId, feedbackId):
        return self.__getNonPaginatedData(f'/events/{eventId}/feedbacks/{feedbackId}')
    
    def getFeedbackByID(self, feedbackId):
        return self.__getNonPaginatedData(f'/feedbacks/{feedbackId}')
    
    def getScaleTeamFeedback(self, scaleTeamId, feedbackId):
        return self.__getNonPaginatedData(f'/scale_teams/{scaleTeamId}/feedbacks/{feedbackId}')
    
    # ------------------- Flags ------------------- #

    def getAllFlags(self, *args):
        return self.__getPaginatedData(f'/flags/', self.__combine_dict(args))
    
    # ------------------- Flashes ------------------- #

    def getAllFlashes(self, *args):
        return self.__getPaginatedData(f'/flashes/', self.__combine_dict(args))
    
    def getFlashByID(self, flashId):
        return self.__getNonPaginatedData(f'/flashes/{flashId}')
    
    # ------------------- Flash Users ------------------- #

    def getFlashFlashUsers(self, flashId, *args):
        return self.__getPaginatedData(f'/flashes/{flashId}/flash_users/', self.__combine_dict(args))
    
    def getAllFlashUsers(self, *args):
        return self.__getPaginatedData(f'/flash_users/', self.__combine_dict(args))
    
    def getFlashFlashUserByID(self, flashId, flashUserId):
        return self.__getNonPaginatedData(f'/flashes/{flashId}/flash_users/{flashUserId}')
    
    def getFlashUserByID(self, flashUserId):
        return self.__getNonPaginatedData(f'/flash_users/{flashUserId}')
    
    # ------------------- Gitlab Users ------------------- #

    def getUserGitlabUsers(self, userId, *args):
        return self.__getPaginatedData(f'/users/{userId}/gitlab_users/', self.__combine_dict(args))
    
    # ------------------- Groups ------------------- #

    def getAllGroups(self, *args):
        return self.__getPaginatedData(f'/groups/', self.__combine_dict(args))
    
    def getUserGroups(self, userId, *args):
        return self.__getPaginatedData(f'/users/{userId}/groups/', self.__combine_dict(args))
    
    def getGroupByID(self, groupId):
        return self.__getNonPaginatedData(f'/groups/{groupId}')
    
    # ------------------- Groups Users ------------------- #

    def getGroupGroupsUsers(self, groupId, *args):
        return self.__getPaginatedData(f'/groups/{groupId}/groups_users/', self.__combine_dict(args))
    
    def getUserGroupsUsers(self, userId, *args):
        return self.__getPaginatedData(f'/users/{userId}/groups_users/', self.__combine_dict(args))
    
    def getAllGroupsUsers(self, *args):  
        return self.__getPaginatedData(f'/groups_users/', self.__combine_dict(args))
    
    def getGroupUserByID(self, groupId, groupsUserId):
        return self.__getNonPaginatedData(f'/groups/{groupId}/groups_users/{groupsUserId}')
    
    def getUserGroupByID(self, userId, groupsUserId):
        return self.__getNonPaginatedData(f'/users/{userId}/groups_users/{groupsUserId}')
    
    # ------------------- internships ------------------- #

    def getAllInternships(self, *args):
        return self.__getPaginatedData(f'/internships/', self.__combine_dict(args))

    def getInternshipByID(self, internshipId):
        return self.__getNonPaginatedData(f'/internships/{internshipId}')
    
    # ------------------- Journals  ------------------- #
    
    def getAllJournals(self, *args):
        return self.__getPaginatedData(f'/journals/', self.__combine_dict(args))
    
    # ------------------- Languages ------------------- #

    def getAllLanguages(self, *args):
        return self.__getPaginatedData(f'/languages/', self.__combine_dict(args))
    
    def getLanguageByID(self, languageId):
        return self.__getNonPaginatedData(f'/languages/{languageId}')
    
    # ------------------- Languages Users ------------------- #

    def getUserLanguagesUsers(self, userId, *args):
        return self.__getPaginatedData(f'/users/{userId}/languages_users/', self.__combine_dict(args))
    
    def getAllLanguagesUsers(self, *args):
        return self.__getPaginatedData(f'/languages_users/', self.__combine_dict(args))
    
    def getUserLanguageByID(self, userId, languageUserId):
        return self.__getNonPaginatedData(f'/users/{userId}/languages_users/{languageUserId}')
    
    def getLanguageUserByID(self, languageUserId):
        return self.__getNonPaginatedData(f'/languages_users/{languageUserId}')
    
    # ------------------- Levels ------------------- #

    def getAllLevels(self, *args):
        return self.__getPaginatedData(f'/levels/', self.__combine_dict(args))
    
    def getCursusLevels(self, cursusId, *args):
        return self.__getPaginatedData(f'/cursus/{cursusId}/levels/', self.__combine_dict(args))
    
    # ------------------- Locations ------------------- #

    def getAllLocations(self, *args):
        return self.__getPaginatedData(f'/locations/', self.__combine_dict(args))
    
    def getUserLocations(self, userId, *args):
        return self.__getPaginatedData(f'/users/{userId}/locations/', self.__combine_dict(args))
    
    def getCampusLocations(self, campusId, *args):
        return self.__getPaginatedData(f'/campus/{campusId}/locations/', self.__combine_dict(args))
    
    def getLocationByID(self, locationId):
        return self.__getNonPaginatedData(f'/locations/{locationId}')
    

    # ------------------- Notes ------------------- #

    def getAllNotes(self, *args):
        return self.__getPaginatedData(f'/notes/', self.__combine_dict(args))
    
    def getUserNotes(self, userId, *args):
        return self.__getPaginatedData(f'/users/{userId}/notes/', self.__combine_dict(args))
    
    def getCampusNotes(self, campusId, *args):
        return self.__getPaginatedData(f'/campus/{campusId}/notes/', self.__combine_dict(args))
    
    def getNoteByID(self, noteId):
        return self.__getNonPaginatedData(f'/notes/{noteId}')

    # ------------------- notions ------------------- #

    def getAllNotions(self, *args):
        return self.__getPaginatedData(f'/notions/', self.__combine_dict(args))
    
    def getCursusNotions(self, cursusId, *args):
        return self.__getPaginatedData(f'/cursus/{cursusId}/notions/', self.__combine_dict(args))
    
    def getTagNotions(self, tagId, *args):
        return self.__getPaginatedData(f'/tags/{tagId}/notions/', self.__combine_dict(args))
    
    def getNotionByID(self, notionId):
        return self.__getNonPaginatedData(f'/notions/{notionId}')

    # ------------------- Offers ------------------- #

    def getAllOffers(self, *args):
        return self.__getPaginatedData(f'/offers/', self.__combine_dict(args))
    
    def getOfferByID(self, offerId):
        return self.__getNonPaginatedData(f'/offers/{offerId}')

    # ------------------- Offers Users ------------------- #

    def getAllOffersUsers(self, *args):
        return self.__getPaginatedData(f'/offers_users/', self.__combine_dict(args))
    
    def getUserOffersUsers(self, userId, *args):
        return self.__getPaginatedData(f'/users/{userId}/offers_users/', self.__combine_dict(args))
    
    def getOfferOffersUsers(self, offerId, *args):
        return self.__getPaginatedData(f'/offers/{offerId}/offers_users/', self.__combine_dict(args))
    
    def getOfferUserByID(self, offerUserId):
        return self.__getNonPaginatedData(f'/offers_users/{offerUserId}')
    
    # ------------------- Params Project sessions rules ------------------- #

    def getAllParamsProjectSessionsRules(self, *args):
        return self.__getPaginatedData(f'/params_project_sessions_rules/', self.__combine_dict(args))
    
    def getParamsProjectSessionsRuleByID(self, paramsProjectSessionsRuleId):
        return self.__getNonPaginatedData(f'/params_project_sessions_rules/{paramsProjectSessionsRuleId}')
    
    def getProjectSessionsRuleParamsProjectSessionsRules(self, projectSessionsRuleId, *args):
        return self.__getPaginatedData(f'/project_sessions_rules/{projectSessionsRuleId}/params_project_sessions_rules/', self.__combine_dict(args))
    
    # ------------------- Partnerships ------------------- #

    def getAllPartnerships(self, *args):
        return self.__getPaginatedData(f'/partnerships/', self.__combine_dict(args))
    
    def getPartnershipByID(self, partnershipId):
        return self.__getNonPaginatedData(f'/partnerships/{partnershipId}')

    # ------------------- Partnerships Users ------------------- #

    def getAllPartnershipsUsers(self, *args):
        return self.__getPaginatedData(f'/partnerships_users/', self.__combine_dict(args))
    
    def getPartnershipPartnershipsUsers(self, partnershipId, *args):
        return self.__getPaginatedData(f'/partnerships/{partnershipId}/partnerships_users/', self.__combine_dict(args))
    
    def getPartnershipUserByID(self, partnershipUserId):
        return self.__getNonPaginatedData(f'/partnerships_users/{partnershipUserId}')
    
    # ------------------- Patronages ------------------- #
    # ------------------- Patronages reports ------------------- #
    # ------------------- Pools ------------------- #
    # ------------------- Products ------------------- #
    # ------------------- Project Data ------------------- #
    # ------------------- Project Sessions ------------------- #
    # ------------------- Project Sessions rules ------------------- #
    # ------------------- Project Sessions skills ------------------- #
    # ------------------- Project ------------------- #

    def getAllProjects(self, *args):
        return self.__getPaginatedData(f'/projects/', self.__combine_dict(args))
    
    def getProjectByID(self, projectId):
        return self.__getNonPaginatedData(f'/projects/{projectId}')
    
    def getCursusProjects(self, cursusId, *args):
        return self.__getPaginatedData(f'/cursus/{cursusId}/projects/', self.__combine_dict(args))
    
    def getProjectProjects(self, projectId, *args):
        return self.__getPaginatedData(f'/projects/{projectId}/projects/', self.__combine_dict(args))
    
    def getMeProjects(self, *args):
        return self.__getPaginatedData(f'/me/projects/', self.__combine_dict(args))
    
    # ------------------- Project users ------------------- #
    
    def getAllProjectsUsers(self, *args):
        return self.__getPaginatedData(f'/projects_users/', self.__combine_dict(args))
    
    def getProjectProjectsUsers(self, projectId, *args):
        return self.__getPaginatedData(f'/projects/{projectId}/projects_users/', self.__combine_dict(args))
    
    def getUserProjectsUsers(self, userId, *args):
        return self.__getPaginatedData(f'/users/{userId}/projects_users/', self.__combine_dict(args))
    
    def getProjectUserByID(self, projectUserId):
        return self.__getNonPaginatedData(f'/projects_users/{projectUserId}')
    
    
    # ------------------- Quests ------------------- #
    # ------------------- Quests users ------------------- #
    # ------------------- Roles  ------------------- #
    # ------------------- Roles entities ------------------- #
    # ------------------- Rules  ------------------- #
    # ------------------- Scale Teams  ------------------- #
    
    def getAllScaleTeams(self, *args):
        return self.__getPaginatedData(f'/scale_teams/', self.__combine_dict(args))
    
    def getScaleTeamByID(self, scaleTeamId):
        return self.__getNonPaginatedData(f'/scale_teams/{scaleTeamId}')
    
    def getProjectSessionScaleTeams(self, projectSessionId, *args):
        return self.__getPaginatedData(f'/project_sessions/{projectSessionId}/scale_teams/', self.__combine_dict(args))
    
    def getProjectScaleTeams(self, projectId, *args):
        return self.__getPaginatedData(f'/projects/{projectId}/scale_teams/', self.__combine_dict(args))
    
    def getUserScaleTeamsAsCorrector(self, userId, *args):
        return self.__getPaginatedData(f'/users/{userId}/scale_teams/as_corrector/', self.__combine_dict(args))
    
    def getUserScaleTeamsAsCorrected(self, userId, *args):
        return self.__getPaginatedData(f'/users/{userId}/scale_teams/as_corrected/', self.__combine_dict(args))
    
    def getMeScaleTeamsAsCorrector(self, *args):
        return self.__getPaginatedData(f'/me/scale_teams/as_corrector/', self.__combine_dict(args))
    
    def getMeScaleTeamsAsCorrected(self, *args):
        return self.__getPaginatedData(f'/me/scale_teams/as_corrected/', self.__combine_dict(args))
    
    def getMeScaleTeams(self, *args):
        return self.__getPaginatedData(f'/me/scale_teams/', self.__combine_dict(args))
    
    def getUserScaleTeams(self, userId, *args):
        return self.__getPaginatedData(f'/users/{userId}/scale_teams/', self.__combine_dict(args))
    
    # ------------------- Scales  ------------------- #
    # ------------------- Scores  ------------------- #
    # ------------------- Skills  ------------------- #
    # ------------------- Slots  ------------------- #
    # ------------------- Squads  ------------------- #
    # ------------------- Subnotions  ------------------- #
    # ------------------- Tags  ------------------- #
    # ------------------- Tags users  ------------------- #
    # ------------------- teams  ------------------- #
    # ------------------- teams uploads  ------------------- #
    # ------------------- teams users  ------------------- #
    # ------------------- titles  ------------------- #
    # ------------------- titles users  ------------------- #
    # ------------------- transactions  ------------------- #
    # ------------------- translations  ------------------- #
    # ------------------- user candidatures  ------------------- #

    def getAllUserCandidatures(self, *args):
        return self.__getPaginatedData(f'/user_candidatures/', self.__combine_dict(args))
    
    def getUserUserCandidature(self, userId):
        return self.__getNonPaginatedData(f'/users/{userId}/user_candidature')
    
    def getUserCandidatureByID(self, userCandidatureId):
        return self.__getNonPaginatedData(f'/user_candidatures/{userCandidatureId}')

    # ------------------- users  ------------------- #
    
    def getUserLocationsStats(self, userId):
        return self.__getNonPaginatedData(f'/users/{userId}/locations_stats')
    
    def getCoalitionUsers(self, coalitionId, *args):
        return self.__getPaginatedData(f'/coalitions/{coalitionId}/users/', self.__combine_dict(args))
    
    def getDashUsers(self, dashId, *args):
        return self.__getPaginatedData(f'/dashes/{dashId}/users/', self.__combine_dict(args))
    
    def getEventUsers(self, eventId, *args):
        return self.__getPaginatedData(f'/events/{eventId}/users/', self.__combine_dict(args))

    def getAccreditationUsers(self, accreditationId, *args):
        return self.__getPaginatedData(f'/accreditations/{accreditationId}/users/', self.__combine_dict(args))
    
    def getTeamUsers(self, teamId, *args):
        return self.__getPaginatedData(f'/teams/{teamId}/users/', self.__combine_dict(args))
    
    def getProjectUsers(self, projectId, *args):
        return self.__getPaginatedData(f'/projects/{projectId}/users/', self.__combine_dict(args))
    
    def getAllUsers(self, *args):
        return self.__getPaginatedData(f'/users/', self.__combine_dict(args))
    
    def getCursusUsers(self, cursusId, *args):
        return self.__getPaginatedData(f'/cursus/{cursusId}/users/', self.__combine_dict(args))
    
    def getCampusUsers(self, campusId, *args):
        return self.__getPaginatedData(f'/campus/{campusId}/users/', self.__combine_dict(args))
    
    def getAchievementUsers(self, achievementId, *args):
        return self.__getPaginatedData(f'/achievements/{achievementId}/users/', self.__combine_dict(args))
    
    def getTitleUsers(self, titleId, *args):
        return self.__getPaginatedData(f'/titles/{titleId}/users/', self.__combine_dict(args))
    
    def getQuestUsers(self, questId, *args):
        return self.__getPaginatedData(f'/quests/{questId}/users/', self.__combine_dict(args))
    
    def getGroupUsers(self, groupId, *args):
        return self.__getPaginatedData(f'/groups/{groupId}/users/', self.__combine_dict(args))
    
    def getUserByID(self, userId):
        return self.__getNonPaginatedData(f'/users/{userId}')
    
    def getMe(self):
        return self.__getNonPaginatedData(f'/me')

    # ------------------- waitlists  ------------------- #

    # -------------------------------------------------- #
