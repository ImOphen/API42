import requests

def sort(arg):
    return(f"sort={arg}")

def filter(arg,value):
    return(f"filter[{arg}]={value}")

def range(arg,value1, value2):
    return(f"range[{arg}]={value1},{value2}")

class Api42():
    def __init__(self, client_id, client_secret, scope):
        self.client_id = client_id
        self.client_secret = client_secret
        self.scope = scope
        self.api_url = 'https://api.intra.42.fr/v2'
        self.token = self.__getTokenHeader()
    
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
    
    def __getPaginatedData(self, url):
        data = []
        Page = 1
        while True:
            r = requests.get(f'{self.api_url}{url}&per_page=100&page={Page}', headers=self.token)
            if r.status_code == 401 and r.json()['message'] == "The access token expired":
                self.token = self.__getTokenHeader()
                continue
            elif r.status_code != 200:
                raise Exception("Error: " + str(r.status_code) + " " + r.text)
            if len(r.json()) == 0:
                break
            data += r.json()
            Page += 1
        return data
    
    def __getNonPaginatedData(self, url):
        r = requests.get(f"{self.api_url}{url}", headers=self.token)
        if r.status_code == 401 and r.json()['message'] == "The access token expired":
            self.token = self.__getTokenHeader()
            return self.__getNonPaginatedData(url)
        elif r.status_code != 200:
            raise Exception("Error: " + str(r.status_code) + " " + r.text)
        return r.json()
    
    def __postData(self, url, data):
        r = requests.post(f"{self.api_url}{url}", headers=self.token, data=data)
        if r.status_code == 401 and r.json()['message'] == "The access token expired":
            self.token = self.__getTokenHeader()
            return self.__postData(url, data)
        elif r.status_code != 201:
            raise Exception("Error: " + str(r.status_code) + " " + r.text)
        return r.json()
    
    def __putData(self, url, data):
        r = requests.put(f"{self.api_url}{url}", headers=self.token, data=data)
        if r.status_code == 401 and r.json()['message'] == "The access token expired":
            self.token = self.__getTokenHeader()
            return self.__putData(url, data)
        elif r.status_code != 204:
            raise Exception("Error: " + str(r.status_code) + " " + r.text)
        return r.json()
    
    def __patchData(self, url, data):
        r = requests.patch(f"{self.api_url}{url}", headers=self.token, data=data)
        if r.status_code == 401 and r.json()['message'] == "The access token expired":
            self.token = self.__getTokenHeader()
            return self.__patchData(url, data)
        elif r.status_code != 204:
            raise Exception("Error: " + str(r.status_code) + " " + r.text)
        return r.json()
    
    def __deleteData(self, url):
        r = requests.delete(f"{self.api_url}{url}", headers=self.token)
        if r.status_code == 401 and r.json()['message'] == "The access token expired":
            self.token = self.__getTokenHeader()
            return self.__deleteData(url)
        elif r.status_code != 204:
            raise Exception("Error: " + str(r.status_code) + " " + r.text)
        return r.json()
    
    # ------------------- GET TOKEN ------------------- #
    
    def getToken(self):
        return self.__getTokenHeader()['Authorization'].split(' ')[1]

    
    # ------------------- Accreditations ------------------- #
    
    def getAllAccreditations(self, query=""):
        return self.__getPaginatedData(f'/accreditations/?{query}')
    
    def getAccreditationByID(self, accreditationId):
        return self.__getNonPaginatedData(f'/accreditations/{accreditationId}')
    
    # ------------------- Achievements ------------------- #
    
    def getAllAchievements(self, query=""):
        return self.__getPaginatedData(f'/achievements/?{query}')
    
    def getAchievementByID(self, achievementId):
        return self.__getNonPaginatedData(f'/achievements/{achievementId}')
    
    def getCursusAchievements(self, cursusId, query=""):
        return self.__getPaginatedData(f'/cursus/{cursusId}/achievements/?{query}')
    
    def getCampusAchievements(self, campusId, query=""):
        return self.__getPaginatedData(f'/campus/{campusId}/achievements/?{query}')
    
    def getTitlesAchievements(self, titleId, query=""):
        return self.__getPaginatedData(f'/titles/{titleId}/achievements/?{query}')
    
    # ------------------- Achievements users ------------------- #
    
    def getAllAchievementsUsers(self, query=""):
        return self.__getPaginatedData(f'/achievements_users/?{query}')
    
    def getAchievementsUsersByID(self, achievementUserId):
        return self.__getNonPaginatedData(f'/achievements_users/{achievementUserId}')
    
    # ------------------- Amendments ------------------- #
    
    def getAllAmendments(self, query=""):
        return self.__getPaginatedData(f'/amendments/?{query}')
    
    def getAmendmentByID(self, amendmentId):
        return self.__getNonPaginatedData(f'/amendments/{amendmentId}')
    
    def getUserAmendments(self, userId, query=""):
        return self.__getPaginatedData(f'/users/{userId}/amendments/?{query}')
    
    def getIntershipsAmendments(self, intershipId, query=""):
        return self.__getPaginatedData(f'/interships/{intershipId}/amendments/?{query}')
    
    # ------------------- Announcements ------------------- #
    
    def getAllAnnouncements(self, query=""):
        return self.__getPaginatedData(f'/announcements/?{query}')
    
    def getAnnouncementByID(self, announcementId):
        return self.__getNonPaginatedData(f'/announcements/{announcementId}')
    
    # ------------------- Anti Grav Units ------------------- #
    
    def getAllAntiGravUnits(self, query=""):
        return self.__getPaginatedData(f'/anti_grav_units/?{query}')
    
    def getAntiGravUnitByID(self, antiGravUnitId):
        return self.__getNonPaginatedData(f'/anti_grav_units/{antiGravUnitId}')
    
    # ------------------- Anti Grav Units Users ------------------- #
    
    def getAllAntiGravUnitsUsers(self, query=""):
        return self.__getPaginatedData(f'/anti_grav_units_users/?{query}')
    
    def getAntiGravUnitsUsersByID(self, antiGravUnitsUserId):
        return self.__getNonPaginatedData(f'/anti_grav_units_users/{antiGravUnitsUserId}')
    
    def getUserAntiGravUnits(self, userId, query=""):
        return self.__getPaginatedData(f'/users/{userId}/anti_grav_units/?{query}')
    
    def getCampusAntiGravUnits(self, campusId, query=""):
        return self.__getPaginatedData(f'/campus/{campusId}/anti_grav_units/?{query}')
    
    # ------------------- Apps ------------------- #
    
    def getAllApps(self, query=""):
        return self.__getPaginatedData(f'/apps/?{query}')
    
    def getAppByID(self, appId):
        return self.__getNonPaginatedData(f'/apps/{appId}')
    
    def getUserApps(self, userId, query=""):
        return self.__getPaginatedData(f'/users/{userId}/apps/?{query}')
    
    # ------------------- Attachments ------------------- #
    
    def getAllAttachments(self, query=""):
        return self.__getPaginatedData(f'/attachments/?{query}')
    
    def getAttachmentByID(self, attachmentId):
        return self.__getNonPaginatedData(f'/attachments/{attachmentId}')
    
    def getProjectSessionsAttachments(self, projectSessionId, query=""):
        return self.__getPaginatedData(f'/project_sessions/{projectSessionId}/attachments/?{query}')
    
    def getProjectAttachments(self, projectId, query=""):
        return self.__getPaginatedData(f'/projects/{projectId}/attachments/?{query}')

    # ------------------- Balances ------------------- #
    
    def getAllBalances(self, query=""):
        return self.__getPaginatedData(f'/balances/?{query}')
    
    def getBalanceByID(self, balanceId):
        return self.__getNonPaginatedData(f'/balances/{balanceId}')
    
    def getPoolsBalances(self, poolId, query=""):
        return self.__getPaginatedData(f'/pools/{poolId}/balances/?{query}')
    
    # ------------------- Bloc deadlines ------------------- #
    
    def getAllBlocDeadlines(self, query=""):
        return self.__getPaginatedData(f'/bloc_deadlines/?{query}')
    
    def getBlocDeadlineByID(self, blocDeadlineId):
        return self.__getNonPaginatedData(f'/bloc_deadlines/{blocDeadlineId}')
    
    def getBlocsBlocDeadlines(self, blocId, query=""):
        return self.__getPaginatedData(f'/blocs/{blocId}/bloc_deadlines/?{query}')
    
    # ------------------- Blocs ------------------- #
    
    def getAllBlocs(self, query=""):
        return self.__getPaginatedData(f'/blocs/?{query}')
    
    def getBlocByID(self, blocId):
        return self.__getNonPaginatedData(f'/blocs/{blocId}')
    
    # ------------------- Broadcasts ------------------- #
    
    def getCampusBroadcasts(self, campusId, query=""):
        return self.__getPaginatedData(f'/campus/{campusId}/broadcasts/?{query}')
    
    # ------------------- campus ------------------- #
    
    def getAllCampuses(self, query=""):
        return self.__getPaginatedData(f'/campus/?{query}')
    
    def getCampusByID(self, campusId):
        return self.__getNonPaginatedData(f'/campus/{campusId}')
    
    def getCampusStats(self, campusId, query=""):
        return self.__getPaginatedData(f'/campus/{campusId}/stats/?{query}')
    
    # ------------------- Certificates ------------------- #
    
    def getAllCertificates(self, query=""):
        return self.__getPaginatedData(f'/certificates/?{query}')
    
    def getCertificateByID(self, certificateId):
        return self.__getNonPaginatedData(f'/certificates/{certificateId}')
    
    # ------------------- Certificates Users ------------------- #
    
    def getAllCertificatesUsers(self, query=""):
        return self.__getPaginatedData(f'/certificates_users/?{query}')
    
    def getCertificateUserByID(self, certificateUserId):
        return self.__getNonPaginatedData(f'/certificates_users/{certificateUserId}')
    
    def getUserCertificates(self, userId, query=""):
        return self.__getPaginatedData(f'/users/{userId}/certificates/?{query}')
    
    def getCertificateCertificatesUsers(self, certificateId, query=""):
        return self.__getPaginatedData(f'/certificates/{certificateId}/certificates_users', query)
    
    # ------------------- Closes ------------------- #
    
    def getAllCloses(self, query=""):
        return self.__getPaginatedData(f'/closes/?{query}')
    
    def getCloseByID(self, closeId):
        return self.__getNonPaginatedData(f'/closes/{closeId}')
    
    def getUserCloses(self, userId, query=""):
        return self.__getPaginatedData(f'/users/{userId}/closes/?{query}')
    
    # ------------------- Coalitions ------------------- #
    
    def getAllCoalitions(self, query=""):
        return self.__getPaginatedData(f'/coalitions/?{query}')
    
    def getCoalitionByID(self, coalitionId):
        return self.__getNonPaginatedData(f'/coalitions/{coalitionId}')
    
    def getUserCoalitions(self, userId, query=""):
        return self.__getPaginatedData(f'/users/{userId}/coalitions/?{query}')
    
    def getBlocsCoalitions(self, blocId, query=""):
        return self.__getPaginatedData(f'/blocs/{blocId}/coalitions/?{query}')
    
    # ------------------- Coalitions Users ------------------- #
    
    def getAllCoalitionsUsers(self, query=""):
        return self.__getPaginatedData(f'/coalitions_users/?{query}')
    
    def getCoalitionUserByID(self, coalitionUserId):
        return self.__getNonPaginatedData(f'/coalitions_users/{coalitionUserId}')
    
    def getUserCoalitionsUsers(self, userId, query=""):
        return self.__getPaginatedData(f'/users/{userId}/coalitions_users/?{query}')
    
    def getCoalitionCoalitionsUsers(self, coalitionId, query=""):
        return self.__getPaginatedData(f'/coalitions/{coalitionId}/coalitions_users/?{query}')
    
    # ------------------- Commands ------------------- #
    
    def getProductsCommands(self, productId, query=""):
        return self.__getPaginatedData(f'/products/{productId}/commands/?{query}')
    
    # ------------------- Community Services ------------------- #
    
    def getAllCommunityServices(self, query=""):
        return self.__getPaginatedData(f'/community_services/?{query}')
    
    def getCommunityServiceByID(self, communityServiceId):
        return self.__getNonPaginatedData(f'/community_services/{communityServiceId}')
    
    def getCloseCommunityServices(self, closeId, query=""):
        return self.__getPaginatedData(f'/closes/{closeId}/community_services/?{query}')
    
    # ------------------- Companies ------------------- #
    
    def getAllCompanies(self, query=""):
        return self.__getPaginatedData(f'/companies/?{query}')
    
    def getCompanyByID(self, companyId):
        return self.__getNonPaginatedData(f'/companies/{companyId}')
    
    def getCompanySubscribedUsers(self, companyId, query=""):
        return self.__getPaginatedData(f'/companies/{companyId}/subscribed_users/?{query}')
    
    def getCompanyInternshipsUsers(self, companyId, query=""):
        return self.__getPaginatedData(f'/companies/{companyId}/internships_users/?{query}')
    
    # ------------------- Correction point historics ------------------- #
    
    def GetUserCorrectionPointHistorics(self, userId, query=""):
        return self.__getPaginatedData(f'/users/{userId}/correction_point_historics/?{query}')
    
    # ------------------- Cursus ------------------- #
    
    def getAllCursus(self, query=""):
        return self.__getPaginatedData(f'/cursus/?{query}')
    
    def getCursusByID(self, cursusId):
        return self.__getNonPaginatedData(f'/cursus/{cursusId}')
    
    # ------------------- Cursus Users ------------------- #
    
    def getAllCursusUsers(self, query=""):
        return self.__getPaginatedData(f'/cursus_users/?{query}')
    
    def getCursusUserByID(self, cursusUserId):
        return self.__getNonPaginatedData(f'/cursus_users/{cursusUserId}')
    
    def getCursusCursusUsers(self, cursusId, query=""):
        return self.__getPaginatedData(f'/cursus/{cursusId}/cursus_users/?{query}')
    
    def getUserCursusUsers(self, userId, query=""):
        return self.__getPaginatedData(f'/users/{userId}/cursus_users/?{query}')
    
    # ------------------- Dashes ------------------- #
    
    def getAllDashes(self, query=""):
        return self.__getPaginatedData(f'/dashes/?{query}')
    
    def getDashByID(self, dashId):
        return self.__getNonPaginatedData(f'/dashes/{dashId}')
    
    # ------------------- Dashes Users ------------------- #
    
    def getAllDashesUsers(self, query=""):
        return self.__getPaginatedData(f'/dashes_users/?{query}')
    
    def getDashesUserByID(self, dashUserId):
        return self.__getNonPaginatedData(f'/dashes_users/{dashUserId}')
    
    def getDashesDashesUsers(self, dashId, query=""):
        return self.__getPaginatedData(f'/dashes/{dashId}/dashes_users/?{query}')
    
    # ------------------- Endpoints ------------------- #
    
    def getAllEndpoints(self, query=""):
        return self.__getPaginatedData(f'/endpoints/?{query}')
    
    def getEndpointByID(self, endpointId):
        return self.__getNonPaginatedData(f'/endpoints/{endpointId}')
    
    # ------------------- Evaluations ------------------- #
    
    def getAllEvaluations(self, query=""):
        return self.__getPaginatedData(f'/evaluations/?{query}')
    
    def getEvaluationByID(self, evaluationId):
        return self.__getNonPaginatedData(f'/evaluations/{evaluationId}')
    
    # ------------------- Events ------------------- #
    
    def getAllEvents(self, query=""):
        return self.__getPaginatedData(f'/events/?{query}')
    
    def getEventByID(self, eventId):
        return self.__getNonPaginatedData(f'/events/{eventId}')
    
    def getCursusEvents(self, cursusId, query=""):
        return self.__getPaginatedData(f'/cursus/{cursusId}/events/?{query}')
    
    def getCampusEvents(self, campusId, query=""):
        return self.__getPaginatedData(f'/campus/{campusId}/events/?{query}')
    
    def getUsersEvents(self, userId, query=""):
        return self.__getPaginatedData(f'/users/{userId}/events/?{query}')
    
    # ------------------- Events Users ------------------- #
    
    def getAllEventsUsers(self, query=""):
        return self.__getPaginatedData(f'/events_users/?{query}')
    
    def getEventsUserByID(self, eventsUserId):
        return self.__getNonPaginatedData(f'/events_users/{eventsUserId}')

    def getUsersEventsUsers(self, userId, query=""):
        return self.__getPaginatedData(f'/users/{userId}/events_users/?{query}')
    
    def getEventsEventsUsers(self, eventId, query=""):
        return self.__getPaginatedData(f'/events/{eventId}/events_users/?{query}')
    
    # ------------------- Exams ------------------- #

    def getAllExams(self, query=""):
        return self.__getPaginatedData(f'/exams/?{query}')
    
    def getExamByID(self, examId):
        return self.__getNonPaginatedData(f'/exams/{examId}')
    
    def getCursusExams(self, cursusId, query=""):
        return self.__getPaginatedData(f'/cursus/{cursusId}/exams/?{query}')
    
    def getCampusExams(self, campusId, query=""):
        return self.__getPaginatedData(f'/campus/{campusId}/exams/?{query}')
    
    def getCampusCursusExams(self, campusId, cursusId, query=""):
        return self.__getPaginatedData(f'/campus/{campusId}/cursus/{cursusId}/exams/?{query}')
    
    def getUserExams(self, userId, query=""):
        return self.__getPaginatedData(f'/users/{userId}/exams/?{query}')
    
    def getProjectExams(self, projectId, query=""):
        return self.__getPaginatedData(f'/projects/{projectId}/exams/?{query}')

    # ------------------- Exams Users ------------------- #

    def getExamExamsUsers(self, examId, query=""):
        return self.__getPaginatedData(f'/exams/{examId}/exams_users/?{query}')
    
    # ------------------- Experiences ------------------- #
    
    def getAllExperiences(self, query=""):
        return self.__getPaginatedData(f'/experiences/?{query}')
    
    def getCampusExperiences(self, campusId, query=""):
        return self.__getPaginatedData(f'/campus/{campusId}/experiences/?{query}')
    
    def getProjectUserExperiences(self, projectUserId, query=""):
        return self.__getPaginatedData(f'/projects_users/{projectUserId}/experiences/?{query}')
    
    def getUserExperiences(self, userId, query=""):
        return self.__getPaginatedData(f'/users/{userId}/experience/?{query}')
    
    def getSkillExperiences(self, skillId, query=""):
        return self.__getPaginatedData(f'/skills/{skillId}/experiences/?{query}')

    def getPartnershipUserExperiences(self, partnershipUserId, query=""):
        return self.__getPaginatedData(f'/partnerships_users/{partnershipUserId}/experiences/?{query}')
    
    def getExperienceByID(self, experienceId):
        return self.__getNonPaginatedData(f'/experiences/{experienceId}')
    

    # ------------------- Expertises ------------------- #

    def getAllExpertises(self, query=""):
        return self.__getPaginatedData(f'/expertises/?{query}')
    
    def getExpertiseByID(self, expertiseId):
        return self.__getNonPaginatedData(f'/expertises/{expertiseId}')
    
    # ------------------- Expertises Users ------------------- #

    def getExpertiseExpertisesUsers(self, expertiseId, query=""):
        return self.__getPaginatedData(f'/expertises/{expertiseId}/expertises_users/?{query}')
    
    def getUserExpertisesUsers(self, userId, query=""):
        return self.__getPaginatedData(f'/users/{userId}/expertises_users/?{query}')
    
    def getAllExpertisesUsers(self, query=""):
        return self.__getPaginatedData(f'/expertises_users/?{query}')
    
    def getExpertiseUserByID(self, expertiseUserId):
        return self.__getNonPaginatedData(f'/expertises_users/{expertiseUserId}')
    
    # ------------------- Feedbacks ------------------- #

    def getEventFeedbacks(self, eventId, query=""):
        return self.__getPaginatedData(f'/events/{eventId}/feedbacks/?{query}')
    
    def getAllFeedbacks(self, query=""):
        return self.__getPaginatedData(f'/feedbacks/?{query}')
    
    def getScaleTeamFeedbacks(self, scaleTeamId, query=""):
        return self.__getPaginatedData(f'/scale_teams/{scaleTeamId}/feedbacks/?{query}')
    
    def getEventFeedback(self, eventId, feedbackId):
        return self.__getNonPaginatedData(f'/events/{eventId}/feedbacks/{feedbackId}')
    
    def getFeedbackByID(self, feedbackId):
        return self.__getNonPaginatedData(f'/feedbacks/{feedbackId}')
    
    def getScaleTeamFeedback(self, scaleTeamId, feedbackId):
        return self.__getNonPaginatedData(f'/scale_teams/{scaleTeamId}/feedbacks/{feedbackId}')
    
    # ------------------- Flags ------------------- #

    def getAllFlags(self, query=""):
        return self.__getPaginatedData(f'/flags/?{query}')
    
    # ------------------- Flashes ------------------- #

    def getAllFlashes(self, query=""):
        return self.__getPaginatedData(f'/flashes/?{query}')
    
    def getFlashByID(self, flashId):
        return self.__getNonPaginatedData(f'/flashes/{flashId}')
    
    # ------------------- Flash Users ------------------- #

    def getFlashFlashUsers(self, flashId, query=""):
        return self.__getPaginatedData(f'/flashes/{flashId}/flash_users/?{query}')
    
    def getAllFlashUsers(self, query=""):
        return self.__getPaginatedData(f'/flash_users/?{query}')
    
    def getFlashFlashUserByID(self, flashId, flashUserId):
        return self.__getNonPaginatedData(f'/flashes/{flashId}/flash_users/{flashUserId}')
    
    def getFlashUserByID(self, flashUserId):
        return self.__getNonPaginatedData(f'/flash_users/{flashUserId}')
    
    # ------------------- Gitlab Users ------------------- #

    def getUserGitlabUsers(self, userId, query=""):
        return self.__getPaginatedData(f'/users/{userId}/gitlab_users/?{query}')
    
    # ------------------- Groups ------------------- #

    def getAllGroups(self, query=""):
        return self.__getPaginatedData(f'/groups/?{query}')
    
    def getUserGroups(self, userId, query=""):
        return self.__getPaginatedData(f'/users/{userId}/groups/?{query}')
    
    def getGroupByID(self, groupId):
        return self.__getNonPaginatedData(f'/groups/{groupId}')
    
    # ------------------- Groups Users ------------------- #

    def getGroupGroupsUsers(self, groupId, query=""):
        return self.__getPaginatedData(f'/groups/{groupId}/groups_users/?{query}')
    
    def getUserGroupsUsers(self, userId, query=""):
        return self.__getPaginatedData(f'/users/{userId}/groups_users/?{query}')
    
    def getAllGroupsUsers(self, query=""):  
        return self.__getPaginatedData(f'/groups_users/?{query}')
    
    def getGroupUserByID(self, groupId, groupsUserId):
        return self.__getNonPaginatedData(f'/groups/{groupId}/groups_users/{groupsUserId}')
    
    def getUserGroupByID(self, userId, groupsUserId):
        return self.__getNonPaginatedData(f'/users/{userId}/groups_users/{groupsUserId}')
    
    # ------------------- internships ------------------- #

    def getAllInternships(self, query=""):
        return self.__getPaginatedData(f'/internships/?{query}')

    def getInternshipByID(self, internshipId):
        return self.__getNonPaginatedData(f'/internships/{internshipId}')
    
    # ------------------- Journals  ------------------- #
    
    def getAllJournals(self, query=""):
        return self.__getPaginatedData(f'/journals/?{query}')
    
    # ------------------- Languages ------------------- #

    def getAllLanguages(self, query=""):
        return self.__getPaginatedData(f'/languages/?{query}')
    
    def getLanguageByID(self, languageId):
        return self.__getNonPaginatedData(f'/languages/{languageId}')
    
    # ------------------- Languages Users ------------------- #

    def getUserLanguagesUsers(self, userId, query=""):
        return self.__getPaginatedData(f'/users/{userId}/languages_users/?{query}')
    
    def getAllLanguagesUsers(self, query=""):
        return self.__getPaginatedData(f'/languages_users/?{query}')
    
    def getUserLanguageByID(self, userId, languageUserId):
        return self.__getNonPaginatedData(f'/users/{userId}/languages_users/{languageUserId}')
    
    def getLanguageUserByID(self, languageUserId):
        return self.__getNonPaginatedData(f'/languages_users/{languageUserId}')
    
    # ------------------- Levels ------------------- #

    def getAllLevels(self, query=""):
        return self.__getPaginatedData(f'/levels/?{query}')
    
    def getCursusLevels(self, cursusId, query=""):
        return self.__getPaginatedData(f'/cursus/{cursusId}/levels/?{query}')
    
    # ------------------- Locations ------------------- #

    def getAllLocations(self, query=""):
        return self.__getPaginatedData(f'/locations/?{query}')
    
    def getUserLocations(self, userId, query=""):
        return self.__getPaginatedData(f'/users/{userId}/locations/?{query}')
    
    def getCampusLocations(self, campusId, query=""):
        return self.__getPaginatedData(f'/campus/{campusId}/locations/?{query}')
    
    def getLocationByID(self, locationId):
        return self.__getNonPaginatedData(f'/locations/{locationId}')
    

    # ------------------- Notes ------------------- #

    def getAllNotes(self, query=""):
        return self.__getPaginatedData(f'/notes/?{query}')
    
    def getUserNotes(self, userId, query=""):
        return self.__getPaginatedData(f'/users/{userId}/notes/?{query}')
    
    def getCampusNotes(self, campusId, query=""):
        return self.__getPaginatedData(f'/campus/{campusId}/notes/?{query}')
    
    def getNoteByID(self, noteId):
        return self.__getNonPaginatedData(f'/notes/{noteId}')

    # ------------------- notions ------------------- #

    def getAllNotions(self, query=""):
        return self.__getPaginatedData(f'/notions/?{query}')
    
    def getCursusNotions(self, cursusId, query=""):
        return self.__getPaginatedData(f'/cursus/{cursusId}/notions/?{query}')
    
    def getTagNotions(self, tagId, query=""):
        return self.__getPaginatedData(f'/tags/{tagId}/notions/?{query}')
    
    def getNotionByID(self, notionId):
        return self.__getNonPaginatedData(f'/notions/{notionId}')

    # ------------------- Offers ------------------- #

    def getAllOffers(self, query=""):
        return self.__getPaginatedData(f'/offers/?{query}')
    
    def getOfferByID(self, offerId):
        return self.__getNonPaginatedData(f'/offers/{offerId}')

    # ------------------- Offers Users ------------------- #

    def getAllOffersUsers(self, query=""):
        return self.__getPaginatedData(f'/offers_users/?{query}')
    
    def getUserOffersUsers(self, userId, query=""):
        return self.__getPaginatedData(f'/users/{userId}/offers_users/?{query}')
    
    def getOfferOffersUsers(self, offerId, query=""):
        return self.__getPaginatedData(f'/offers/{offerId}/offers_users/?{query}')
    
    def getOfferUserByID(self, offerUserId):
        return self.__getNonPaginatedData(f'/offers_users/{offerUserId}')
    
    # ------------------- Params Project sessions rules ------------------- #

    def getAllParamsProjectSessionsRules(self, query=""):
        return self.__getPaginatedData(f'/params_project_sessions_rules/?{query}')
    
    def getParamsProjectSessionsRuleByID(self, paramsProjectSessionsRuleId):
        return self.__getNonPaginatedData(f'/params_project_sessions_rules/{paramsProjectSessionsRuleId}')
    
    def getProjectSessionsRuleParamsProjectSessionsRules(self, projectSessionsRuleId, query=""):
        return self.__getPaginatedData(f'/project_sessions_rules/{projectSessionsRuleId}/params_project_sessions_rules/?{query}')
    
    # ------------------- Partnerships ------------------- #

    def getAllPartnerships(self, query=""):
        return self.__getPaginatedData(f'/partnerships/?{query}')
    
    def getPartnershipByID(self, partnershipId):
        return self.__getNonPaginatedData(f'/partnerships/{partnershipId}')

    # ------------------- Partnerships Users ------------------- #

    def getAllPartnershipsUsers(self, query=""):
        return self.__getPaginatedData(f'/partnerships_users/?{query}')
    
    def getPartnershipPartnershipsUsers(self, partnershipId, query=""):
        return self.__getPaginatedData(f'/partnerships/{partnershipId}/partnerships_users/?{query}')
    
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

    def getAllProjects(self, query=""):
        return self.__getPaginatedData(f'/projects/?{query}')
    
    def getProjectByID(self, projectId):
        return self.__getNonPaginatedData(f'/projects/{projectId}')
    
    def getCursusProjects(self, cursusId, query=""):
        return self.__getPaginatedData(f'/cursus/{cursusId}/projects/?{query}')
    
    def getProjectProjects(self, projectId, query=""):
        return self.__getPaginatedData(f'/projects/{projectId}/projects/?{query}')
    
    def getMeProjects(self, query=""):
        return self.__getPaginatedData(f'/me/projects/?{query}')
    
    # ------------------- Project users ------------------- #
    
    def getAllProjectsUsers(self, query=""):
        return self.__getPaginatedData(f'/projects_users/?{query}')
    
    def getProjectProjectsUsers(self, projectId, query=""):
        return self.__getPaginatedData(f'/projects/{projectId}/projects_users/?{query}')
    
    def getUserProjectsUsers(self, userId, query=""):
        return self.__getPaginatedData(f'/users/{userId}/projects_users/?{query}')
    
    def getProjectUserByID(self, projectUserId):
        return self.__getNonPaginatedData(f'/projects_users/{projectUserId}')
    
    
    # ------------------- Quests ------------------- #
    # ------------------- Quests users ------------------- #
    # ------------------- Roles  ------------------- #
    # ------------------- Roles entities ------------------- #
    # ------------------- Rules  ------------------- #
    # ------------------- Scale Teams  ------------------- #
    
    def getAllScaleTeams(self, query=""):
        return self.__getPaginatedData(f'/scale_teams/?{query}')
    
    def getScaleTeamByID(self, scaleTeamId):
        return self.__getNonPaginatedData(f'/scale_teams/{scaleTeamId}')
    
    def getProjectSessionScaleTeams(self, projectSessionId, query=""):
        return self.__getPaginatedData(f'/project_sessions/{projectSessionId}/scale_teams/?{query}')
    
    def getProjectScaleTeams(self, projectId, query=""):
        return self.__getPaginatedData(f'/projects/{projectId}/scale_teams/?{query}')
    
    def getUserScaleTeamsAsCorrector(self, userId, query=""):
        return self.__getPaginatedData(f'/users/{userId}/scale_teams/as_corrector/?{query}')
    
    def getUserScaleTeamsAsCorrected(self, userId, query=""):
        return self.__getPaginatedData(f'/users/{userId}/scale_teams/as_corrected/?{query}')
    
    def getMeScaleTeamsAsCorrector(self, query=""):
        return self.__getPaginatedData(f'/me/scale_teams/as_corrector/?{query}')
    
    def getMeScaleTeamsAsCorrected(self, query=""):
        return self.__getPaginatedData(f'/me/scale_teams/as_corrected/?{query}')
    
    def getMeScaleTeams(self, query=""):
        return self.__getPaginatedData(f'/me/scale_teams/?{query}')
    
    def getUserScaleTeams(self, userId, query=""):
        return self.__getPaginatedData(f'/users/{userId}/scale_teams/?{query}')
    
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

    def getAllUserCandidatures(self, query=""):
        return self.__getPaginatedData(f'/user_candidatures/?{query}')
    
    def getUserUserCandidature(self, userId):
        return self.__getNonPaginatedData(f'/users/{userId}/user_candidature')
    
    def getUserCandidatureByID(self, userCandidatureId):
        return self.__getNonPaginatedData(f'/user_candidatures/{userCandidatureId}')

    # ------------------- users  ------------------- #
    
    def getUserLocationsStats(self, userId):
        return self.__getNonPaginatedData(f'/users/{userId}/locations_stats')
    
    def getCoalitionUsers(self, coalitionId, query=""):
        return self.__getPaginatedData(f'/coalitions/{coalitionId}/users/?{query}')
    
    def getDashUsers(self, dashId, query=""):
        return self.__getPaginatedData(f'/dashes/{dashId}/users/?{query}')
    
    def getEventUsers(self, eventId, query=""):
        return self.__getPaginatedData(f'/events/{eventId}/users/?{query}')

    def getAccreditationUsers(self, accreditationId, query=""):
        return self.__getPaginatedData(f'/accreditations/{accreditationId}/users/?{query}')
    
    def getTeamUsers(self, teamId, query=""):
        return self.__getPaginatedData(f'/teams/{teamId}/users/?{query}')
    
    def getProjectUsers(self, projectId, query=""):
        return self.__getPaginatedData(f'/projects/{projectId}/users/?{query}')
    
    def getAllUsers(self, query=""):
        return self.__getPaginatedData(f'/users/?{query}')
    
    def getCursusUsers(self, cursusId, query=""):
        return self.__getPaginatedData(f'/cursus/{cursusId}/users/?{query}')
    
    def getCampusUsers(self, campusId, query=""):
        return self.__getPaginatedData(f'/campus/{campusId}/users/?{query}')
    
    def getAchievementUsers(self, achievementId, query=""):
        return self.__getPaginatedData(f'/achievements/{achievementId}/users/?{query}')
    
    def getTitleUsers(self, titleId, query=""):
        return self.__getPaginatedData(f'/titles/{titleId}/users/?{query}')
    
    def getQuestUsers(self, questId, query=""):
        return self.__getPaginatedData(f'/quests/{questId}/users/?{query}')
    
    def getGroupUsers(self, groupId, query=""):
        return self.__getPaginatedData(f'/groups/{groupId}/users/?{query}')
    
    def getUserByID(self, userId):
        return self.__getNonPaginatedData(f'/users/{userId}')
    
    def getMe(self):
        return self.__getNonPaginatedData(f'/me')

    # ------------------- waitlists  ------------------- #

    # -------------------------------------------------- #
