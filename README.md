# API42

I have made a 42 API python wrapper, where it allows you to make api calls with ease.

> it's very early and doesn't have all the routes and methods, it's a work in progress ^^, Any feedback or ideas are appreciated

    - Support for python 3.6 and above
    - Multi-threading for faster requests [BETA]
    - Easy to use
    - Reliability and stability ( requests are resent automatically in case of failure because of Rate limit or Token expiration )
    - No need to use a token, it will be generated automatically and kept track of
    

## Installation :  
  ``pip install api42``
  
## Examples :

 in this example, we can find people searching for a minishell group in Khouribga ( campus 16 )
<img width="1105" alt="image" src="https://user-images.githubusercontent.com/43254081/220220830-d9ba5048-5a34-4de1-be6d-1495687b72d9.png">


## Methods :
```python
    # ------------------- GET TOKEN ------------------- #
    getToken()
    # ------------------- Accreditations ------------------- #
    getAllAccreditations(*args)
    getAccreditationByID(accreditationId)
    # ------------------- Achievements ------------------- #
    getAllAchievements(*args)
    getAchievementByID(achievementId)
    getCursusAchievements(cursusId, *args)
    getCampusAchievements(campusId, *args)
    getTitlesAchievements(titleId, *args)
    # ------------------- Achievements users ------------------- #
    getAllAchievementsUsers(*args)
    getAchievementsUsersByID(achievementUserId)
    # ------------------- Amendments ------------------- #
    getAllAmendments(*args)
    getAmendmentByID(amendmentId)
    getUserAmendments(userId, *args)
    getIntershipsAmendments(intershipId, *args)
    # ------------------- Announcements ------------------- #
    getAllAnnouncements(*args)
    getAnnouncementByID(announcementId)
    # ------------------- Anti Grav Units ------------------- #
    getAllAntiGravUnits(*args)
    getAntiGravUnitByID(antiGravUnitId)
    # ------------------- Anti Grav Units Users ------------------- #
    getAllAntiGravUnitsUsers(*args)
    getAntiGravUnitsUsersByID(antiGravUnitsUserId)
    getUserAntiGravUnits(userId, *args)
    getCampusAntiGravUnits(campusId, *args)
    # ------------------- Apps ------------------- #
    getAllApps(*args)
    getAppByID(appId)
    getUserApps(userId, *args)
    # ------------------- Attachments ------------------- #
    getAllAttachments(*args)
    getAttachmentByID(attachmentId)
    getProjectSessionsAttachments(projectSessionId, *args)
    getProjectAttachments(projectId, *args)
    # ------------------- Balances ------------------- #
    getAllBalances(*args)
    getBalanceByID(balanceId)
    getPoolsBalances(poolId, *args)
    # ------------------- Bloc deadlines ------------------- #
    getAllBlocDeadlines(*args)
    getBlocDeadlineByID(blocDeadlineId)
    getBlocsBlocDeadlines(blocId, *args)
    # ------------------- Blocs ------------------- #
    getAllBlocs(*args)
    getBlocByID(blocId)
    # ------------------- Broadcasts ------------------- #
    getCampusBroadcasts(campusId, *args)
    # ------------------- campus ------------------- #
    getAllCampuses(*args)
    getCampusByID(campusId)
    getCampusStats(campusId, *args)
    # ------------------- Certificates ------------------- #
    getAllCertificates(*args)
    getCertificateByID(certificateId)
    # ------------------- Certificates Users ------------------- #
    getAllCertificatesUsers(*args)
    getCertificateUserByID(certificateUserId)
    getUserCertificates(userId, *args)
    getCertificateCertificatesUsers(certificateId, *args)
    # ------------------- Closes ------------------- #
    getAllCloses(*args)
    getCloseByID(closeId)
    getUserCloses(userId, *args)
    # ------------------- Coalitions ------------------- #
    getAllCoalitions(*args)
    getCoalitionByID(coalitionId)
    getUserCoalitions(userId, *args)
    getBlocsCoalitions(blocId, *args)
    # ------------------- Coalitions Users ------------------- #
    getAllCoalitionsUsers(*args)
    getCoalitionUserByID(coalitionUserId)
    getUserCoalitionsUsers(userId, *args)
    getCoalitionCoalitionsUsers(coalitionId, *args)
    # ------------------- Commands ------------------- #
    getProductsCommands(productId, *args)
    # ------------------- Community Services ------------------- #
    getAllCommunityServices(*args)
    getCommunityServiceByID(communityServiceId)
    getCloseCommunityServices(closeId, *args)
    # ------------------- Companies ------------------- #
    getAllCompanies(*args)
    getCompanyByID(companyId)
    getCompanySubscribedUsers(companyId, *args)
    getCompanyInternshipsUsers(companyId, *args)
    # ------------------- Correction point historics ------------------- #
    GetUserCorrectionPointHistorics(userId, *args)
    # ------------------- Cursus ------------------- #
    getAllCursus(*args)
    getCursusByID(cursusId)
    # ------------------- Cursus Users ------------------- #
    getAllCursusUsers(*args)
    getCursusUserByID(cursusUserId)
    getCursusCursusUsers(cursusId, *args)
    getUserCursusUsers(userId, *args)
    # ------------------- Dashes ------------------- #
    getAllDashes(*args)
    getDashByID(dashId)
    # ------------------- Dashes Users ------------------- #
    getAllDashesUsers(*args)
    getDashesUserByID(dashUserId)
    getDashesDashesUsers(dashId, *args)
    # ------------------- Endpoints ------------------- #
    getAllEndpoints(*args)
    getEndpointByID(endpointId)
    # ------------------- Evaluations ------------------- #
    getAllEvaluations(*args)
    getEvaluationByID(evaluationId)
    # ------------------- Events ------------------- #
    getAllEvents(*args)
    getEventByID(eventId)
    getCursusEvents(cursusId, *args)
    getCampusEvents(campusId, *args)
    getUsersEvents(userId, *args)
    # ------------------- Events Users ------------------- #
    getAllEventsUsers(*args)
    getEventsUserByID(eventsUserId)
    getUsersEventsUsers(userId, *args)
    getEventsEventsUsers(eventId, *args)
    # ------------------- Exams ------------------- #
    getAllExams(*args)
    getExamByID(examId)
    getCursusExams(cursusId, *args)
    getCampusExams(campusId, *args)
    getCampusCursusExams(campusId, cursusId, *args)
    getUserExams(userId, *args)
    getProjectExams(projectId, *args)
    # ------------------- Exams Users ------------------- #
    getExamExamsUsers(examId, *args)
    # ------------------- Experiences ------------------- #
    getAllExperiences(*args)
    getCampusExperiences(campusId, *args)
    getProjectUserExperiences(projectUserId, *args)
    getUserExperiences(userId, *args)
    getSkillExperiences(skillId, *args)
    getPartnershipUserExperiences(partnershipUserId, *args)
    getExperienceByID(experienceId)
    # ------------------- Expertises ------------------- #
    getAllExpertises(*args)
    getExpertiseByID(expertiseId)
    # ------------------- Expertises Users ------------------- #
    getExpertiseExpertisesUsers(expertiseId, *args)
    getUserExpertisesUsers(userId, *args)
    getAllExpertisesUsers(*args)
    getExpertiseUserByID(expertiseUserId)
    # ------------------- Feedbacks ------------------- #
    getEventFeedbacks(eventId, *args)
    getAllFeedbacks(*args)
    getScaleTeamFeedbacks(scaleTeamId, *args)
    getEventFeedback(eventId, feedbackId)
    getFeedbackByID(feedbackId)
    getScaleTeamFeedback(scaleTeamId, feedbackId)
    # ------------------- Flags ------------------- #
    getAllFlags(*args)
    # ------------------- Flashes ------------------- #
    getAllFlashes(*args)
    getFlashByID(flashId)
    # ------------------- Flash Users ------------------- #
    getFlashFlashUsers(flashId, *args)
    getAllFlashUsers(*args)
    getFlashFlashUserByID(flashId, flashUserId)
    getFlashUserByID(flashUserId)
    # ------------------- Gitlab Users ------------------- #
    getUserGitlabUsers(userId, *args)
    # ------------------- Groups ------------------- #
    getAllGroups(*args)
    getUserGroups(userId, *args)
    getGroupByID(groupId)
    # ------------------- Groups Users ------------------- #
    getGroupGroupsUsers(groupId, *args)
    getUserGroupsUsers(userId, *args)
    getAllGroupsUsers(*args)  
    getGroupUserByID(groupId, groupsUserId)
    getUserGroupByID(userId, groupsUserId)
    # ------------------- internships ------------------- #
    getAllInternships(*args)
    getInternshipByID(internshipId)
    # ------------------- Journals  ------------------- #
    getAllJournals(*args)
    # ------------------- Languages ------------------- #
    getAllLanguages(*args)
    getLanguageByID(languageId)
    # ------------------- Languages Users ------------------- #
    getUserLanguagesUsers(userId, *args)
    getAllLanguagesUsers(*args)
    getUserLanguageByID(userId, languageUserId)
    getLanguageUserByID(languageUserId)
    # ------------------- Levels ------------------- #
    getAllLevels(*args)
    getCursusLevels(cursusId, *args)
    # ------------------- Locations ------------------- #
    getAllLocations(*args)
    getUserLocations(userId, *args)
    getCampusLocations(campusId, *args)
    getLocationByID(locationId)
    # ------------------- Notes ------------------- #
    getAllNotes(*args)
    getUserNotes(userId, *args)
    getCampusNotes(campusId, *args)
    getNoteByID(noteId)
    # ------------------- notions ------------------- #
    getAllNotions(*args)
    getCursusNotions(cursusId, *args)
    getTagNotions(tagId, *args)
    getNotionByID(notionId)
    # ------------------- Offers ------------------- #
    getAllOffers(*args)
    getOfferByID(offerId)
    # ------------------- Offers Users ------------------- #
    getAllOffersUsers(*args)
    getUserOffersUsers(userId, *args)
    getOfferOffersUsers(offerId, *args)
    getOfferUserByID(offerUserId)
    # ------------------- Params Project sessions rules ------------------- #
    getAllParamsProjectSessionsRules(*args)
    getParamsProjectSessionsRuleByID(paramsProjectSessionsRuleId)
    getProjectSessionsRuleParamsProjectSessionsRules(projectSessionsRuleId, *args)
    # ------------------- Partnerships ------------------- #
    getAllPartnerships(*args)
    getPartnershipByID(partnershipId)
    # ------------------- Partnerships Users ------------------- #
    getAllPartnershipsUsers(*args)
    getPartnershipPartnershipsUsers(partnershipId, *args)
    getPartnershipUserByID(partnershipUserId)
    # ------------------- Patronages ------------------- #
    # ------------------- Patronages reports ------------------- #
    # ------------------- Pools ------------------- #
    # ------------------- Products ------------------- #
    # ------------------- Project Data ------------------- #
    # ------------------- Project Sessions ------------------- #
    # ------------------- Project Sessions rules ------------------- #
    # ------------------- Project Sessions skills ------------------- #
    # ------------------- Project ------------------- #
    getAllProjects(*args)
    getProjectByID(projectId)
    getCursusProjects(cursusId, *args)
    getProjectProjects(projectId, *args)
    getMeProjects(*args)
    # ------------------- Project users ------------------- #
    getAllProjectsUsers(*args)
    getProjectProjectsUsers(projectId, *args)
    getUserProjectsUsers(userId, *args)
    getProjectUserByID(projectUserId)
    # ------------------- Quests ------------------- #
    # ------------------- Quests users ------------------- #
    # ------------------- Roles  ------------------- #
    # ------------------- Roles entities ------------------- #
    # ------------------- Rules  ------------------- #
    # ------------------- Scale Teams  ------------------- #
    getAllScaleTeams(*args)
    getScaleTeamByID(scaleTeamId)
    getProjectSessionScaleTeams(projectSessionId, *args)
    getProjectScaleTeams(projectId, *args)
    getUserScaleTeamsAsCorrector(userId, *args)
    getUserScaleTeamsAsCorrected(userId, *args)
    getMeScaleTeamsAsCorrector(*args)
    getMeScaleTeamsAsCorrected(*args)
    getMeScaleTeams(*args)
    getUserScaleTeams(userId, *args)
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
    getAllUserCandidatures(*args)
    getUserUserCandidature(userId)
    getUserCandidatureByID(userCandidatureId)
    # ------------------- users  ------------------- #
    getUserLocationsStats(userId)
    getCoalitionUsers(coalitionId, *args)
    getDashUsers(dashId, *args)
    getEventUsers(eventId, *args)
    getAccreditationUsers(accreditationId, *args)
    getTeamUsers(teamId, *args)
    getProjectUsers(projectId, *args)
    getAllUsers(*args)
    getCursusUsers(cursusId, *args)
    getCampusUsers(campusId, *args)
    getAchievementUsers(achievementId, *args)
    getTitleUsers(titleId, *args)
    getQuestUsers(questId, *args)
    getGroupUsers(groupId, *args)
    getUserByID(userId)
    getMe()
    # ------------------- waitlists  ------------------- #
    # ------------------- custom -------------------- #
    getCustomPaginatedData(url, *args)
    getCustomNonPaginatedData(url)
    # -------------------------------------------------- #
```