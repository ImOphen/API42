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
     getToken():
    # ------------------- Accreditations ------------------- #
    getAllAccreditations(query=""):
    getAccreditationByID(accreditationId):
    # ------------------- Achievements ------------------- #
    getAllAchievements(query=""):
    getAchievementByID(achievementId):
    getCursusAchievements(cursusId, query=""):
    getCampusAchievements(campusId, query=""):
    getTitlesAchievements(titleId, query=""):
    # ------------------- Achievements users ------------------- #
    getAllAchievementsUsers(query=""):
    getAchievementsUsersByID(achievementUserId):
    # ------------------- Amendments ------------------- #
    getAllAmendments(query=""):
    getAmendmentByID(amendmentId):
    getUserAmendments(userId, query=""):
    getIntershipsAmendments(intershipId, query=""):
    # ------------------- Announcements ------------------- #
    getAllAnnouncements(query=""):
    getAnnouncementByID(announcementId):
    # ------------------- Anti Grav Units ------------------- #
    getAllAntiGravUnits(query=""):
    getAntiGravUnitByID(antiGravUnitId):
    # ------------------- Anti Grav Units Users ------------------- #
    getAllAntiGravUnitsUsers(query=""):
    getAntiGravUnitsUsersByID(antiGravUnitsUserId):
    getUserAntiGravUnits(userId, query=""):
    getCampusAntiGravUnits(campusId, query=""):
    # ------------------- Apps ------------------- #
    getAllApps(query=""):
    getAppByID(appId):
    getUserApps(userId, query=""):
    # ------------------- Attachments ------------------- #
    getAllAttachments(query=""):
    getAttachmentByID(attachmentId):
    getProjectSessionsAttachments(projectSessionId, query=""):
    getProjectAttachments(projectId, query=""):
    # ------------------- Balances ------------------- #
    getAllBalances(query=""):
    getBalanceByID(balanceId):
    getPoolsBalances(poolId, query=""):
    # ------------------- Bloc deadlines ------------------- #
    getAllBlocDeadlines(query=""):
    getBlocDeadlineByID(blocDeadlineId):
    getBlocsBlocDeadlines(blocId, query=""):
    # ------------------- Blocs ------------------- #
    getAllBlocs(query=""):
    getBlocByID(blocId):
    # ------------------- Broadcasts ------------------- #
    getCampusBroadcasts(campusId, query=""):
    # ------------------- campus ------------------- #
    getAllCampuses(query=""):
    getCampusByID(campusId):
    getCampusStats(campusId, query=""):
    # ------------------- Certificates ------------------- #
    getAllCertificates(query=""):
    getCertificateByID(certificateId):
    # ------------------- Certificates Users ------------------- #
    getAllCertificatesUsers(query=""):
    getCertificateUserByID(certificateUserId):
    getUserCertificates(userId, query=""):
    getCertificateCertificatesUsers(certificateId, query=""):
    # ------------------- Closes ------------------- #
    getAllCloses(query=""):
    getCloseByID(closeId):
    getUserCloses(userId, query=""):
    # ------------------- Coalitions ------------------- #
    getAllCoalitions(query=""):
    getCoalitionByID(coalitionId):
    getUserCoalitions(userId, query=""):
    getBlocsCoalitions(blocId, query=""):
    # ------------------- Coalitions Users ------------------- #
    getAllCoalitionsUsers(query=""):
    getCoalitionUserByID(coalitionUserId):
    getUserCoalitionsUsers(userId, query=""):
    getCoalitionCoalitionsUsers(coalitionId, query=""):
    # ------------------- Commands ------------------- #
    getProductsCommands(productId, query=""):
    # ------------------- Community Services ------------------- #
    getAllCommunityServices(query=""):
    getCommunityServiceByID(communityServiceId):
    getCloseCommunityServices(closeId, query=""):
    # ------------------- Companies ------------------- #
    getAllCompanies(query=""):
    getCompanyByID(companyId):
    getCompanySubscribedUsers(companyId, query=""):
    getCompanyInternshipsUsers(companyId, query=""):
    # ------------------- Correction point historics ------------------- #
    GetUserCorrectionPointHistorics(userId, query=""):
    # ------------------- Cursus ------------------- #
    getAllCursus(query=""):
    getCursusByID(cursusId):
    # ------------------- Cursus Users ------------------- #
    getAllCursusUsers(query=""):
    getCursusUserByID(cursusUserId):
    getCursusCursusUsers(cursusId, query=""):
    getUserCursusUsers(userId, query=""):
    # ------------------- Dashes ------------------- #
    getAllDashes(query=""):
    getDashByID(dashId):
    # ------------------- Dashes Users ------------------- #
    getAllDashesUsers(query=""):
    getDashesUserByID(dashUserId):
    getDashesDashesUsers(dashId, query=""):
    # ------------------- Endpoints ------------------- #
    getAllEndpoints(query=""):
    getEndpointByID(endpointId):
    # ------------------- Evaluations ------------------- #
    getAllEvaluations(query=""):
    getEvaluationByID(evaluationId):
    # ------------------- Events ------------------- #
    getAllEvents(query=""):
    getEventByID(eventId):
    getCursusEvents(cursusId, query=""):
    getCampusEvents(campusId, query=""):
    getUsersEvents(userId, query=""):
    # ------------------- Events Users ------------------- #
    getAllEventsUsers(query=""):
    getEventsUserByID(eventsUserId):
    getUsersEventsUsers(userId, query=""):
    getEventsEventsUsers(eventId, query=""):
    # ------------------- Exams ------------------- #
    getAllExams(query=""):
    getExamByID(examId):
    getCursusExams(cursusId, query=""):
    getCampusExams(campusId, query=""):
    getCampusCursusExams(campusId, cursusId, query=""):
    getUserExams(userId, query=""):
    getProjectExams(projectId, query=""):
    # ------------------- Exams Users ------------------- #
    getExamExamsUsers(examId, query=""):
    # ------------------- Experiences ------------------- #
    getAllExperiences(query=""):
    getCampusExperiences(campusId, query=""):
    getProjectUserExperiences(projectUserId, query=""):
    getUserExperiences(userId, query=""):
    getSkillExperiences(skillId, query=""):
    getPartnershipUserExperiences(partnershipUserId, query=""):
    getExperienceByID(experienceId):
    # ------------------- Expertises ------------------- #
    getAllExpertises(query=""):
    getExpertiseByID(expertiseId):
    # ------------------- Expertises Users ------------------- #
    getExpertiseExpertisesUsers(expertiseId, query=""):
    getUserExpertisesUsers(userId, query=""):
    getAllExpertisesUsers(query=""):
    getExpertiseUserByID(expertiseUserId):
    # ------------------- Feedbacks ------------------- #
    getEventFeedbacks(eventId, query=""):
    getAllFeedbacks(query=""):
    getScaleTeamFeedbacks(scaleTeamId, query=""):
    getEventFeedback(eventId, feedbackId):
    getFeedbackByID(feedbackId):
    getScaleTeamFeedback(scaleTeamId, feedbackId):
    # ------------------- Flags ------------------- #
    getAllFlags(query=""):
    # ------------------- Flashes ------------------- #
    getAllFlashes(query=""):
    getFlashByID(flashId):
    # ------------------- Flash Users ------------------- #
    getFlashFlashUsers(flashId, query=""):
    getAllFlashUsers(query=""):
    getFlashFlashUserByID(flashId, flashUserId):
    getFlashUserByID(flashUserId):
    # ------------------- Gitlab Users ------------------- #
    getUserGitlabUsers(userId, query=""):
    # ------------------- Groups ------------------- #
    getAllGroups(query=""):
    getUserGroups(userId, query=""):
    getGroupByID(groupId):
    # ------------------- Groups Users ------------------- #
    getGroupGroupsUsers(groupId, query=""):
    getUserGroupsUsers(userId, query=""):
    getAllGroupsUsers(query=""):  
    getGroupUserByID(groupId, groupsUserId):
    getUserGroupByID(userId, groupsUserId):
    # ------------------- internships ------------------- #
    getAllInternships(query=""):
    getInternshipByID(internshipId):
    # ------------------- Journals  ------------------- #
    getAllJournals(query=""):
    # ------------------- Languages ------------------- #
    getAllLanguages(query=""):
    getLanguageByID(languageId):
    # ------------------- Languages Users ------------------- #
    getUserLanguagesUsers(userId, query=""):
    getAllLanguagesUsers(query=""):
    getUserLanguageByID(userId, languageUserId):
    getLanguageUserByID(languageUserId):
    # ------------------- Levels ------------------- #
    getAllLevels(query=""):
    getCursusLevels(cursusId, query=""):
    # ------------------- Locations ------------------- #
    getAllLocations(query=""):
    getUserLocations(userId, query=""):
    getCampusLocations(campusId, query=""):
    getLocationByID(locationId):
    # ------------------- Notes ------------------- #
    getAllNotes(query=""):
    getUserNotes(userId, query=""):
    getCampusNotes(campusId, query=""):
    getNoteByID(noteId):
    # ------------------- notions ------------------- #
    getAllNotions(query=""):
    getCursusNotions(cursusId, query=""):
    getTagNotions(tagId, query=""):
    getNotionByID(notionId):
    # ------------------- Offers ------------------- #
    getAllOffers(query=""):
    getOfferByID(offerId):
    # ------------------- Offers Users ------------------- #
    getAllOffersUsers(query=""):
    getUserOffersUsers(userId, query=""):
    getOfferOffersUsers(offerId, query=""):
    getOfferUserByID(offerUserId):
    # ------------------- Params Project sessions rules ------------------- #
    getAllParamsProjectSessionsRules(query=""):
    getParamsProjectSessionsRuleByID(paramsProjectSessionsRuleId):
    getProjectSessionsRuleParamsProjectSessionsRules(projectSessionsRuleId, query=""):
    # ------------------- Partnerships ------------------- #
    getAllPartnerships(query=""):
    getPartnershipByID(partnershipId):
    # ------------------- Partnerships Users ------------------- #
    getAllPartnershipsUsers(query=""):
    getPartnershipPartnershipsUsers(partnershipId, query=""):
    getPartnershipUserByID(partnershipUserId):
    # ------------------- Patronages ------------------- #
    # ------------------- Patronages reports ------------------- #
    # ------------------- Pools ------------------- #
    # ------------------- Products ------------------- #
    # ------------------- Project Data ------------------- #
    # ------------------- Project Sessions ------------------- #
    # ------------------- Project Sessions rules ------------------- #
    # ------------------- Project Sessions skills ------------------- #
    # ------------------- Project ------------------- #
    getAllProjects(query=""):
    getProjectByID(projectId):
    getCursusProjects(cursusId, query=""):
    getProjectProjects(projectId, query=""):
    getMeProjects(query=""):
    # ------------------- Project users ------------------- #
    getAllProjectsUsers(query=""):
    getProjectProjectsUsers(projectId, query=""):
    getUserProjectsUsers(userId, query=""):
    getProjectUserByID(projectUserId):
    # ------------------- Quests ------------------- #
    # ------------------- Quests users ------------------- #
    # ------------------- Roles  ------------------- #
    # ------------------- Roles entities ------------------- #
    # ------------------- Rules  ------------------- #
    # ------------------- Scale Teams  ------------------- #
    getAllScaleTeams(query=""):
    getScaleTeamByID(scaleTeamId):
    getProjectSessionScaleTeams(projectSessionId, query=""):
    getProjectScaleTeams(projectId, query=""):
    getUserScaleTeamsAsCorrector(userId, query=""):
    getUserScaleTeamsAsCorrected(userId, query=""):
    getMeScaleTeamsAsCorrector(query=""):
    getMeScaleTeamsAsCorrected(query=""):
    getMeScaleTeams(query=""):
    getUserScaleTeams(userId, query=""):
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
    getAllUserCandidatures(query=""):
    getUserUserCandidature(userId):
    getUserCandidatureByID(userCandidatureId):
    # ------------------- users  ------------------- #
    getUserLocationsStats(userId):
    getCoalitionUsers(coalitionId, query=""):
    getDashUsers(dashId, query=""):
    getEventUsers(eventId, query=""):
    getAccreditationUsers(accreditationId, query=""):
    getTeamUsers(teamId, query=""):
    getProjectUsers(projectId, query=""):
    getAllUsers(query=""):
    getCursusUsers(cursusId, query=""):
    getCampusUsers(campusId, query=""):
    getAchievementUsers(achievementId, query=""):
    getTitleUsers(titleId, query=""):
    getQuestUsers(questId, query=""):
    getGroupUsers(groupId, query=""):
    getUserByID(userId):
    getMe():```
