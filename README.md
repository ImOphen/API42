# API42

I have made a 42 API python wrapper, where it allows you to make api calls with ease.

> it's very early and doesn't have all the routes and methods, it's a work in progress ^^, Any feedback or ideas are appreciated

## Installation :  
  ``pip install api42``
  
## Examples :

 in this example, we can find people searching for a minishell group in Khouribga ( campus 16 )
<img width="1087" alt="image" src="https://user-images.githubusercontent.com/43254081/220191609-01976679-fbd5-4717-9abb-48a18c71a088.png">

## Methods :
```python
    # ------------------- get TOKEN ------------------- #
        getToken()
    # ------------------- Accreditations ------------------- #
        getAllAccreditations(*params)
        getAccreditationByID(accreditationId)
    # ------------------- Achievements ------------------- #
        getAllAchievements(*params)
        getAchievementByID(achievementId)
        getCursusAchievements(cursusId, *params)
        getCampusAchievements(campusId, *params)
        getTitlesAchievements(titleId, *params)
    # ------------------- Achievements users ------------------- #
        getAllAchievementsUsers(*params)
        getAchievementsUsersByID(achievementUserId)
    # ------------------- Amendments ------------------- #
        getAllAmendments(*params)
        getAmendmentByID(amendmentId)
        getUserAmendments(userId, *params)
        getIntershipsAmendments(intershipId, *params)
    # ------------------- Announcements ------------------- #
        getAllAnnouncements(*params)
        getAnnouncementByID(announcementId)
    # ------------------- Anti Grav Units ------------------- #
        getAllAntiGravUnits(*params)
        getAntiGravUnitByID(antiGravUnitId)
    # ------------------- Anti Grav Units Users ------------------- #
        getAllAntiGravUnitsUsers(*params)
        getAntiGravUnitsUsersByID(antiGravUnitsUserId)
        getUserAntiGravUnits(userId, *params)
        getCampusAntiGravUnits(campusId, *params)
    # ------------------- Apps ------------------- #
        getAllApps(*params)
        getAppByID(appId)
        getUserApps(userId, *params)
    # ------------------- Attachments ------------------- #
        getAllAttachments(*params)
        getAttachmentByID(attachmentId)
        getProjectSessionsAttachments(projectSessionId, *params)
        getProjectAttachments(projectId, *params)
    # ------------------- Balances ------------------- #
        getAllBalances(*params)
        getBalanceByID(balanceId)
        getPoolsBalances(poolId, *params)
    # ------------------- Bloc deadlines ------------------- #
        getAllBlocDeadlines(*params)
        getBlocDeadlineByID(blocDeadlineId)
        getBlocsBlocDeadlines(blocId, *params)
    # ------------------- Blocs ------------------- #
        getAllBlocs(*params)
        getBlocByID(blocId)
    # ------------------- Broadcasts ------------------- #
        getCampusBroadcasts(campusId, *params)
    # ------------------- campus ------------------- #
        getAllCampuses(*params)
        getCampusByID(campusId)
        getCampusStats(campusId, *params)
    # ------------------- Certificates ------------------- #
        getAllCertificates(*params)
        getCertificateByID(certificateId)
    # ------------------- Certificates Users ------------------- #
        getAllCertificatesUsers(*params)
        getCertificateUserByID(certificateUserId)
        getUserCertificates(userId, *params)
        getCertificateCertificatesUsers(certificateId, *params)
    # ------------------- Closes ------------------- #
        getAllCloses(*params)
        getCloseByID(closeId)
        getUserCloses(userId, *params)
    # ------------------- Coalitions ------------------- #
        getAllCoalitions(*params)
        getCoalitionByID(coalitionId)
        getUserCoalitions(userId, *params)
        getBlocsCoalitions(blocId, *params)
    # ------------------- Coalitions Users ------------------- #
        getAllCoalitionsUsers(*params)
        getCoalitionUserByID(coalitionUserId)
        getUserCoalitionsUsers(userId, *params)
        getCoalitionCoalitionsUsers(coalitionId, *params)
    # ------------------- Commands ------------------- #
        getProductsCommands(productId, *params)
    # ------------------- Community Services ------------------- #
        getAllCommunityServices(*params)
        getCommunityServiceByID(communityServiceId)
        getCloseCommunityServices(closeId, *params)
    # ------------------- Companies ------------------- #
        getAllCompanies(*params)
        getCompanyByID(companyId)
        getCompanySubscribedUsers(companyId, *params)
        getCompanyInternshipsUsers(companyId, *params)
    # ------------------- Correction point historics ------------------- #
        getUserCorrectionPointHistorics(userId, *params)
    # ------------------- Cursus ------------------- #
        getAllCursus(*params)
        getCursusByID(cursusId)
    # ------------------- Cursus Users ------------------- #
        getAllCursusUsers(*params)
        getCursusUserByID(cursusUserId)
        getCursusCursusUsers(cursusId, *params)
        getUserCursusUsers(userId, *params)
    # ------------------- Dashes ------------------- #
        getAllDashes(*params)
        getDashByID(dashId)
    # ------------------- Dashes Users ------------------- #
        getAllDashesUsers(*params)
        getDashesUserByID(dashUserId)
        getDashesDashesUsers(dashId, *params)
    # ------------------- Endpoints ------------------- #
        getAllEndpoints(*params)
        getEndpointByID(endpointId)
    # ------------------- Evaluations ------------------- #
        getAllEvaluations(*params)
        getEvaluationByID(evaluationId)
    # ------------------- Events ------------------- #
        getAllEvents(*params)
        getEventByID(eventId)
        getCursusEvents(cursusId, *params)
        getCampusEvents(campusId, *params)
        getUsersEvents(userId, *params)
    # ------------------- Events Users ------------------- #
        getAllEventsUsers(*params)
        getEventsUserByID(eventsUserId)
        getUsersEventsUsers(userId, *params)
        getEventsEventsUsers(eventId, *params)
    # ------------------- Exams ------------------- #
        getAllExams(*params)
        getExamByID(examId)
        getCursusExams(cursusId, *params)
        getCampusExams(campusId, *params)
        getCampusCursusExams(campusId, cursusId, *params)
        getUserExams(userId, *params)
        getProjectExams(projectId, *params)
    # ------------------- Exams Users ------------------- #
        getExamExamsUsers(examId, *params)
    # ------------------- Experiences ------------------- #
        getAllExperiences(*params)
        getCampusExperiences(campusId, *params)
        getProjectUserExperiences(projectUserId, *params)
        getUserExperiences(userId, *params)
        getSkillExperiences(skillId, *params)
        getPartnershipUserExperiences(partnershipUserId, *params)
        getExperienceByID(experienceId)
    # ------------------- Expertises ------------------- #
        getAllExpertises(*params)
        getExpertiseByID(expertiseId)
    # ------------------- Expertises Users ------------------- #
        getExpertiseExpertisesUsers(expertiseId, *params)
        getUserExpertisesUsers(userId, *params)
        getAllExpertisesUsers(*params)
        getExpertiseUserByID(expertiseUserId)
    # ------------------- Feedbacks ------------------- #
        getEventFeedbacks(eventId, *params)
        getAllFeedbacks(*params)
        getScaleTeamFeedbacks(scaleTeamId, *params)
        getEventFeedback(eventId, feedbackId)
        getFeedbackByID(feedbackId)
        getScaleTeamFeedback(scaleTeamId, feedbackId)
    # ------------------- Flags ------------------- #
        getAllFlags(*params)
    # ------------------- Flashes ------------------- #
        getAllFlashes(*params)
        getFlashByID(flashId)
    # ------------------- Flash Users ------------------- #
        getFlashFlashUsers(flashId, *params)
        getAllFlashUsers(*params)
        getFlashFlashUserByID(flashId, flashUserId)
        getFlashUserByID(flashUserId)
    # ------------------- Gitlab Users ------------------- #
        getUserGitlabUsers(userId, *params)
    # ------------------- Groups ------------------- #
        getAllGroups(*params)
        getUserGroups(userId, *params)
        getGroupByID(groupId)
    # ------------------- Groups Users ------------------- #
        getGroupGroupsUsers(groupId, *params)
        getUserGroupsUsers(userId, *params)
        getAllGroupsUsers(*params)  
        getGroupUserByID(groupId, groupsUserId)
        getUserGroupByID(userId, groupsUserId)
    # ------------------- internships ------------------- #
        getAllInternships(*params)
        getInternshipByID(internshipId)
    # ------------------- Journals  ------------------- #
        getAllJournals(*params)
    # ------------------- Languages ------------------- #
        getAllLanguages(*params)
        getLanguageByID(languageId)
    # ------------------- Languages Users ------------------- #
        getUserLanguagesUsers(userId, *params)
        getAllLanguagesUsers(*params)
        getUserLanguageByID(userId, languageUserId)
        getLanguageUserByID(languageUserId)
    # ------------------- Levels ------------------- #
        getAllLevels(*params)
        getCursusLevels(cursusId, *params)
    # ------------------- Locations ------------------- #
        getAllLocations(*params)
        getUserLocations(userId, *params)
        getCampusLocations(campusId, *params)
        getLocationByID(locationId)
    # ------------------- Notes ------------------- #
        getAllNotes(*params)
        getUserNotes(userId, *params)
        getCampusNotes(campusId, *params)
        getNoteByID(noteId)
    # ------------------- notions ------------------- #
        getAllNotions(*params)
        getCursusNotions(cursusId, *params)
        getTagNotions(tagId, *params)
        getNotionByID(notionId)
    # ------------------- Offers ------------------- #
        getAllOffers(*params)
        getOfferByID(offerId)
    # ------------------- Offers Users ------------------- #
        getAllOffersUsers(*params)
        getUserOffersUsers(userId, *params)
        getOfferOffersUsers(offerId, *params)
        getOfferUserByID(offerUserId)
    # ------------------- Params Project sessions rules ------------------- #
        getAllParamsProjectSessionsRules(*params)
        getParamsProjectSessionsRuleByID(paramsProjectSessionsRuleId)
        getProjectSessionsRuleParamsProjectSessionsRules(projectSessionsRuleId, *params)
    # ------------------- Partnerships ------------------- #
        getAllPartnerships(*params)
        getPartnershipByID(partnershipId)
    # ------------------- Partnerships Users ------------------- #
        getAllPartnershipsUsers(*params)
        getPartnershipPartnershipsUsers(partnershipId, *params)
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
        getAllProjects(*params)
        getProjectByID(projectId)
        getCursusProjects(cursusId, *params)
        getProjectProjects(projectId, *params)
        getMeProjects(*params)
    # ------------------- Project users ------------------- #
        getAllProjectsUsers(*params)
        getProjectProjectsUsers(projectId, *params)
        getUserProjectsUsers(userId, *params)
        getProjectUserByID(projectUserId)
    # ------------------- Quests ------------------- #
    # ------------------- Quests users ------------------- #
    # ------------------- Roles  ------------------- #
    # ------------------- Roles entities ------------------- #
    # ------------------- Rules  ------------------- #
    # ------------------- Scale Teams  ------------------- #
        getAllScaleTeams(*params)
        getScaleTeamByID(scaleTeamId)
        getProjectSessionScaleTeams(projectSessionId, *params)
        getProjectScaleTeams(projectId, *params)
        getUserScaleTeamsAsCorrector(userId, *params)
        getUserScaleTeamsAsCorrected(userId, *params)
        getMeScaleTeamsAsCorrector(*params)
        getMeScaleTeamsAsCorrected(*params)
        getMeScaleTeams(*params)
        getUserScaleTeams(userId, *params)
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
        getAllUserCandidatures(*params)
        getUserUserCandidature(userId)
        getUserCandidatureByID(userCandidatureId)
    # ------------------- users  ------------------- #
        getUserLocationsStats(userId)
        getCoalitionUsers(coalitionId, *params)
        getDashUsers(dashId, *params)
        getEventUsers(eventId, *params)
        getAccreditationUsers(accreditationId, *params)
        getTeamUsers(teamId, *params)
        getProjectUsers(projectId, *params)
        getAllUsers(*params)
        getCursusUsers(cursusId, *params)
        getCampusUsers(campusId, *params)
        getAchievementUsers(achievementId, *params)
        getTitleUsers(titleId, *params)
        getQuestUsers(questId, *params)
        getGroupUsers(groupId, *params)
        getUserByID(userId)
        getMe()
    # ------------------- waitlists  ------------------- #
    # -------------------------------------------------- #
    ```
