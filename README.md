# API42

I have made a 42 API python wrapper, where it allows you to make api calls with ease.

> it's very early and doesn't have all the routes and methods, it's a work in progress ^^, Any feedback or ideas are appreciated

## Installation :  
  ``pip install api42``
  
## Examples :

 in this example, we can find people searching for a minishell group in Khouribga ( campus 16 )
<img width="1177" alt="image" src="https://user-images.githubusercontent.com/43254081/220163247-849152c6-9443-454d-85e6-70f0a790bf6a.png">


## Methods :
```python
    def getToken(self):
    # ------------------- Accreditations ------------------- #
    def getAllAccreditations(self, query=""):
    def getAccreditationByID(self, accreditationId):
    # ------------------- Achievements ------------------- #
    def getAllAchievements(self, query=""):
    def getAchievementByID(self, achievementId):
    def getCursusAchievements(self, cursusId, query=""):
    def getCampusAchievements(self, campusId, query=""):
    def getTitlesAchievements(self, titleId, query=""):
    # ------------------- Achievements users ------------------- #
    def getAllAchievementsUsers(self, query=""):
    def getAchievementsUsersByID(self, achievementUserId):
    # ------------------- Amendments ------------------- #
    def getAllAmendments(self, query=""):
    def getAmendmentByID(self, amendmentId):
    def getUserAmendments(self, userId, query=""):
    def getIntershipsAmendments(self, intershipId, query=""):
    # ------------------- Announcements ------------------- #
    def getAllAnnouncements(self, query=""):
    def getAnnouncementByID(self, announcementId):
    # ------------------- Anti Grav Units ------------------- #
    def getAllAntiGravUnits(self, query=""):
    def getAntiGravUnitByID(self, antiGravUnitId):
    # ------------------- Anti Grav Units Users ------------------- #
    def getAllAntiGravUnitsUsers(self, query=""):
    def getAntiGravUnitsUsersByID(self, antiGravUnitsUserId):
    def getUserAntiGravUnits(self, userId, query=""):
    def getCampusAntiGravUnits(self, campusId, query=""):
    # ------------------- Apps ------------------- #
    def getAllApps(self, query=""):
    def getAppByID(self, appId):
    def getUserApps(self, userId, query=""):
    # ------------------- Attachments ------------------- #
    def getAllAttachments(self, query=""):
    def getAttachmentByID(self, attachmentId):
    def getProjectSessionsAttachments(self, projectSessionId, query=""):
    def getProjectAttachments(self, projectId, query=""):
    # ------------------- Balances ------------------- #
    def getAllBalances(self, query=""):
    def getBalanceByID(self, balanceId):
    def getPoolsBalances(self, poolId, query=""):
    # ------------------- Bloc deadlines ------------------- #
    def getAllBlocDeadlines(self, query=""):
    def getBlocDeadlineByID(self, blocDeadlineId):
    def getBlocsBlocDeadlines(self, blocId, query=""):
    # ------------------- Blocs ------------------- #
    def getAllBlocs(self, query=""):
    def getBlocByID(self, blocId):
    # ------------------- Broadcasts ------------------- #
    def getCampusBroadcasts(self, campusId, query=""):
    # ------------------- campus ------------------- #
    def getAllCampuses(self, query=""):
    def getCampusByID(self, campusId):
    def getCampusStats(self, campusId, query=""):
    # ------------------- Certificates ------------------- #
    def getAllCertificates(self, query=""):
    def getCertificateByID(self, certificateId):
    # ------------------- Certificates Users ------------------- #
    def getAllCertificatesUsers(self, query=""):
    def getCertificateUserByID(self, certificateUserId):
    def getUserCertificates(self, userId, query=""):
    def getCertificateCertificatesUsers(self, certificateId, query=""):
    # ------------------- Closes ------------------- #
    def getAllCloses(self, query=""):
    def getCloseByID(self, closeId):
    def getUserCloses(self, userId, query=""):
    # ------------------- Coalitions ------------------- #
    def getAllCoalitions(self, query=""):
    def getCoalitionByID(self, coalitionId):
    def getUserCoalitions(self, userId, query=""):
    def getBlocsCoalitions(self, blocId, query=""):
    # ------------------- Coalitions Users ------------------- #
    def getAllCoalitionsUsers(self, query=""):
    def getCoalitionUserByID(self, coalitionUserId):
    def getUserCoalitionsUsers(self, userId, query=""):
    def getCoalitionCoalitionsUsers(self, coalitionId, query=""):
    # ------------------- Commands ------------------- #
    def getProductsCommands(self, productId, query=""):
    # ------------------- Community Services ------------------- #
    def getAllCommunityServices(self, query=""):
    def getCommunityServiceByID(self, communityServiceId):
    def getCloseCommunityServices(self, closeId, query=""):
    # ------------------- Companies ------------------- #
    def getAllCompanies(self, query=""):
    def getCompanyByID(self, companyId):
    def getCompanySubscribedUsers(self, companyId, query=""):
    def getCompanyInternshipsUsers(self, companyId, query=""):
    # ------------------- Correction point historics ------------------- #
    def GetUserCorrectionPointHistorics(self, userId, query=""):
    # ------------------- Cursus ------------------- #
    def getAllCursus(self, query=""):
    def getCursusByID(self, cursusId):
    # ------------------- Cursus Users ------------------- #
    def getAllCursusUsers(self, query=""):
    def getCursusUserByID(self, cursusUserId):
    def getCursusCursusUsers(self, cursusId, query=""):
    def getUserCursusUsers(self, userId, query=""):
    # ------------------- Dashes ------------------- #
    def getAllDashes(self, query=""):
    def getDashByID(self, dashId):
    # ------------------- Dashes Users ------------------- #
    def getAllDashesUsers(self, query=""):
    def getDashesUserByID(self, dashUserId):
    def getDashesDashesUsers(self, dashId, query=""):
    # ------------------- Endpoints ------------------- #
    def getAllEndpoints(self, query=""):
    def getEndpointByID(self, endpointId):
    # ------------------- Evaluations ------------------- #
    def getAllEvaluations(self, query=""):
    def getEvaluationByID(self, evaluationId):
    # ------------------- Events ------------------- #
    def getAllEvents(self, query=""):
    def getEventByID(self, eventId):
    def getCursusEvents(self, cursusId, query=""):
    def getCampusEvents(self, campusId, query=""):
    def getUsersEvents(self, userId, query=""):
    # ------------------- Events Users ------------------- #
    def getAllEventsUsers(self, query=""):
    def getEventsUserByID(self, eventsUserId):
    def getUsersEventsUsers(self, userId, query=""):
    def getEventsEventsUsers(self, eventId, query=""):
    # ------------------- Exams ------------------- #
    def getAllExams(self, query=""):
    def getExamByID(self, examId):
    def getCursusExams(self, cursusId, query=""):
    def getCampusExams(self, campusId, query=""):
    def getCampusCursusExams(self, campusId, cursusId, query=""):
    def getUserExams(self, userId, query=""):
    def getProjectExams(self, projectId, query=""):
    # ------------------- Exams Users ------------------- #
    def getExamExamsUsers(self, examId, query=""):
    # ------------------- Experiences ------------------- #
    def getAllExperiences(self, query=""):
    def getCampusExperiences(self, campusId, query=""):
    def getProjectUserExperiences(self, projectUserId, query=""):
    def getUserExperiences(self, userId, query=""):
    def getSkillExperiences(self, skillId, query=""):
    def getPartnershipUserExperiences(self, partnershipUserId, query=""):
    def getExperienceByID(self, experienceId):
    # ------------------- Expertises ------------------- #
    def getAllExpertises(self, query=""):
    def getExpertiseByID(self, expertiseId):
    # ------------------- Expertises Users ------------------- #
    def getExpertiseExpertisesUsers(self, expertiseId, query=""):
    def getUserExpertisesUsers(self, userId, query=""):
    def getAllExpertisesUsers(self, query=""):
    def getExpertiseUserByID(self, expertiseUserId):
    # ------------------- Feedbacks ------------------- #
    def getEventFeedbacks(self, eventId, query=""):
    def getAllFeedbacks(self, query=""):
    def getScaleTeamFeedbacks(self, scaleTeamId, query=""):
    def getEventFeedback(self, eventId, feedbackId):
    def getFeedbackByID(self, feedbackId):
    def getScaleTeamFeedback(self, scaleTeamId, feedbackId):
    # ------------------- Flags ------------------- #
    def getAllFlags(self, query=""):
    # ------------------- Flashes ------------------- #
    def getAllFlashes(self, query=""):
    def getFlashByID(self, flashId):
    # ------------------- Flash Users ------------------- #
    def getFlashFlashUsers(self, flashId, query=""):
    def getAllFlashUsers(self, query=""):
    def getFlashFlashUserByID(self, flashId, flashUserId):
    def getFlashUserByID(self, flashUserId):
    # ------------------- Gitlab Users ------------------- #
    def getUserGitlabUsers(self, userId, query=""):
    # ------------------- Groups ------------------- #
    def getAllGroups(self, query=""):
    def getUserGroups(self, userId, query=""):
    def getGroupByID(self, groupId):
    # ------------------- Groups Users ------------------- #
    def getGroupGroupsUsers(self, groupId, query=""):
    def getUserGroupsUsers(self, userId, query=""):
    def getAllGroupsUsers(self, query=""):  
    def getGroupUserByID(self, groupId, groupsUserId):
    def getUserGroupByID(self, userId, groupsUserId):
    # ------------------- internships ------------------- #
    def getAllInternships(self, query=""):
    def getInternshipByID(self, internshipId):
    # ------------------- Journals  ------------------- #
    def getAllJournals(self, query=""):
    # ------------------- Languages ------------------- #
    def getAllLanguages(self, query=""):
    def getLanguageByID(self, languageId):
    # ------------------- Languages Users ------------------- #
    def getUserLanguagesUsers(self, userId, query=""):
    def getAllLanguagesUsers(self, query=""):
    def getUserLanguageByID(self, userId, languageUserId):
    def getLanguageUserByID(self, languageUserId):
    # ------------------- Levels ------------------- #
    def getAllLevels(self, query=""):
    def getCursusLevels(self, cursusId, query=""):
    # ------------------- Locations ------------------- #
    def getAllLocations(self, query=""):
    def getUserLocations(self, userId, query=""):
    def getCampusLocations(self, campusId, query=""):
    def getLocationByID(self, locationId):
    # ------------------- Notes ------------------- #
    def getAllNotes(self, query=""):
    def getUserNotes(self, userId, query=""):
    def getCampusNotes(self, campusId, query=""):
    def getNoteByID(self, noteId):
    # ------------------- notions ------------------- #
    def getAllNotions(self, query=""):
    def getCursusNotions(self, cursusId, query=""):
    def getTagNotions(self, tagId, query=""):
    def getNotionByID(self, notionId):
    # ------------------- Offers ------------------- #
    def getAllOffers(self, query=""):
    def getOfferByID(self, offerId):
    # ------------------- Offers Users ------------------- #
    def getAllOffersUsers(self, query=""):
    def getUserOffersUsers(self, userId, query=""):
    def getOfferOffersUsers(self, offerId, query=""):
    def getOfferUserByID(self, offerUserId):
    # ------------------- Params Project sessions rules ------------------- #
    def getAllParamsProjectSessionsRules(self, query=""):
    def getParamsProjectSessionsRuleByID(self, paramsProjectSessionsRuleId):
    def getProjectSessionsRuleParamsProjectSessionsRules(self, projectSessionsRuleId, query=""):
    # ------------------- Partnerships ------------------- #
    def getAllPartnerships(self, query=""):
    def getPartnershipByID(self, partnershipId):
    # ------------------- Partnerships Users ------------------- #
    def getAllPartnershipsUsers(self, query=""):
    def getPartnershipPartnershipsUsers(self, partnershipId, query=""):
    def getPartnershipUserByID(self, partnershipUserId):
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
    def getProjectByID(self, projectId):
    def getCursusProjects(self, cursusId, query=""):
    def getProjectProjects(self, projectId, query=""):
    def getMeProjects(self, query=""):
    # ------------------- Project users ------------------- #
    def getAllProjectsUsers(self, query=""):
    def getProjectProjectsUsers(self, projectId, query=""):
    def getUserProjectsUsers(self, userId, query=""):
    def getProjectUserByID(self, projectUserId):
    # ------------------- Quests ------------------- #
    # ------------------- Quests users ------------------- #
    # ------------------- Roles  ------------------- #
    # ------------------- Roles entities ------------------- #
    # ------------------- Rules  ------------------- #
    # ------------------- Scale Teams  ------------------- #
    def getAllScaleTeams(self, query=""):
    def getScaleTeamByID(self, scaleTeamId):
    def getProjectSessionScaleTeams(self, projectSessionId, query=""):
    def getProjectScaleTeams(self, projectId, query=""):
    def getUserScaleTeamsAsCorrector(self, userId, query=""):
    def getUserScaleTeamsAsCorrected(self, userId, query=""):
    def getMeScaleTeamsAsCorrector(self, query=""):
    def getMeScaleTeamsAsCorrected(self, query=""):
    def getMeScaleTeams(self, query=""):
    def getUserScaleTeams(self, userId, query=""):
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
    def getUserUserCandidature(self, userId):
    def getUserCandidatureByID(self, userCandidatureId):
    # ------------------- users  ------------------- #
    def getUserLocationsStats(self, userId):
    def getCoalitionUsers(self, coalitionId, query=""):
    def getDashUsers(self, dashId, query=""):
    def getEventUsers(self, eventId, query=""):
    def getAccreditationUsers(self, accreditationId, query=""):
    def getTeamUsers(self, teamId, query=""):
    def getProjectUsers(self, projectId, query=""):
    def getAllUsers(self, query=""):
    def getCursusUsers(self, cursusId, query=""):
    def getCampusUsers(self, campusId, query=""):
    def getAchievementUsers(self, achievementId, query=""):
    def getTitleUsers(self, titleId, query=""):
    def getQuestUsers(self, questId, query=""):
    def getGroupUsers(self, groupId, query=""):
    def getUserByID(self, userId):
    def getMe(self):```
