# AI-Powered Cybersecurity Risk Assessment Portal
## Basecamp Project Plan

**Project Manager:** Sai Charan Nagilla  
**Team:** Smart Secure Innovators (Sai Charan Nagilla, Pranav Dara, Sandeep Reddy Manthena)  
**Duration:** October 10, 2025 - April 10, 2026 (6 months)  
**Budget:** $63,250  
**Status:** In Progress (50% complete as of Nov 23, 2025)

---

## 📋 TO-DO ITEMS & TASKS

### Phase 1: Planning & Charter (Oct 10-31, 2025) - COMPLETED ✅

#### Week 1: Team Formation & Kickoff
- [x] Finalize team roster and roles
- [x] Conduct project kickoff meeting
- [x] Establish communication protocols (Basecamp, GitHub, email)
- [x] Define project scope and objectives
- **Assigned to:** All team members  
- **Status:** Completed Oct 20, 2025

#### Week 2: Project Charter Development
- [x] Conduct stakeholder interviews
- [x] Develop detailed project charter
- [x] Perform financial analysis (cost, benefit, payback, NPV)
- [x] Identify risks and mitigation strategies
- [x] Get charter approved by instructor
- **Assigned to:** Sai Charan Nagilla (Lead), Pranav Dara, Sandeep Reddy Manthena  
- **Status:** Completed Oct 31, 2025
- **Deliverable:** PROJECT_CHARTER.md, Cost_Calculations_Payback_NPV.md

**Phase 1 Summary:**
- Financial Metrics Verified:
  - Total Cost: $63,250 (Labor $58,250 + Supplies $3,000 + Misc $2,000)
  - Annual Benefit: $65,000
  - Payback Period: 0.97 years (~12 months)
  - NPV (3 years @ 8%): $104,270
  - ROI: 102.8%
- Project Timeline: 6 months (Oct 10 - Apr 10, 2026)
- Critical Path Identified: Planning → Design → Dev → Testing → Final

---

### Phase 2: Design & Requirements (Nov 1-20, 2025) - COMPLETED ✅

#### Week 3: System Architecture Design
- [x] Define system architecture (microservices pattern)
- [x] Design AI/ML model pipeline
- [x] Create database schema
- [x] Design REST API endpoints
- [x] Plan frontend UI/UX
- **Assigned to:** Pranav Dara (Lead), Sai Charan Nagilla  
- **Status:** Completed Nov 10, 2025
- **Deliverable:** Architecture diagrams, API_DOCUMENTATION.md

#### Week 4: Requirements Specification
- [x] Document functional requirements
- [x] Document non-functional requirements (security, performance, scalability)
- [x] Create user stories and acceptance criteria
- [x] Define deployment infrastructure (AWS, Docker)
- **Assigned to:** Sandeep Reddy Manthena (Lead), Pranav Dara  
- **Status:** Completed Nov 20, 2025
- **Deliverable:** DEPLOYMENT_GUIDE.md, technical specifications

**Phase 2 Summary:**
- System Architecture: AI Model + Flask Backend + React Frontend + Dashboard
- Database: Vulnerability data, risk assessments, user profiles
- Security Requirements: Data encryption, authentication, authorization
- Scalability: Auto-scaling groups, load balancing, caching

---

### Phase 3: Development & Implementation (Nov 21, 2025 - Mar 10, 2026) - IN PROGRESS 🔄

#### Sprint 1: AI Model Development (Nov 21 - Dec 5)
- [x] Set up Python environment and dependencies
- [x] Create vulnerability classifier skeleton
- [x] Implement feature extraction pipeline
- [x] Integrate scikit-learn and ML libraries
- [ ] Train initial model on sample data
- [ ] Achieve baseline accuracy (>85%)
- **Assigned to:** Sai Charan Nagilla (Lead), Pranav Dara  
- **Status:** 60% complete
- **Deliverable:** src/ai_model/vulnerability_classifier.py (committed)

#### Sprint 2: Backend Development (Dec 6-20)
- [x] Set up Flask web server
- [x] Create project structure and routing
- [x] Implement CORS for frontend integration
- [x] Design API endpoints (/health, /api/scan, /api/risk-report)
- [ ] Implement authentication & authorization
- [ ] Create database connectors
- **Assigned to:** Pranav Dara (Lead), Sandeep Reddy Manthena  
- **Status:** 50% complete
- **Deliverable:** src/web_app/backend/app.py (committed)

#### Sprint 3: Frontend Development (Dec 21 - Jan 20, 2026)
- [x] Initialize React application
- [x] Set up routing and navigation
- [x] Create component structure (Dashboard, Reports, Settings)
- [ ] Build UI components (forms, charts, tables)
- [ ] Implement state management (Redux/Context)
- [ ] Connect to backend API
- **Assigned to:** Sandeep Reddy Manthena (Lead), Sai Charan Nagilla  
- **Status:** 40% complete
- **Deliverable:** src/web_app/frontend/package.json (committed)

#### Sprint 4: Dashboard & Visualization (Jan 21 - Feb 15, 2026)
- [x] Create risk dashboard module
- [ ] Implement real-time vulnerability tracking
- [ ] Build risk score visualization charts
- [ ] Create report generation engine
- [ ] Integrate data from AI model and backend
- **Assigned to:** Sai Charan Nagilla (Lead), Pranav Dara  
- **Status:** 30% complete
- **Deliverable:** src/dashboard/dashboard.py (committed)

#### Development Notes:
- **Code Repository:** https://github.com/saicharan714/Smart-Secure-Innovators_AI-Powered-Cybersecurity-Risk-Assessment-Portal
- **Tech Stack:** Python (Flask), React, PostgreSQL, Docker, AWS
- **Commits to Date:**
  1. "Initial project setup for final project - Smart Secure Innovators" (20 files, 3591 insertions)
  2. "Added initial AI model code and web app framework" (4 files, 247 insertions)
  3. "Final project version with full documentation, model, and portal" (6 files, 313 insertions)

---

### Phase 4: Testing & QA (Mar 11-31, 2026) - NOT STARTED

#### Unit Testing
- [ ] Write unit tests for AI model (target: >90% code coverage)
- [ ] Write unit tests for API endpoints
- [ ] Write unit tests for frontend components
- [ ] Achieve >85% test pass rate
- **Assigned to:** Pranav Dara (Lead)  
- **Expected Start:** Mar 11, 2026
- **Deliverable:** tests/model_tests/test_classifier.py, tests/api_tests/test_endpoints.py, tests/ui_tests/test_components.py

#### Integration Testing
- [ ] Test AI model → Backend integration
- [ ] Test Backend → Frontend integration
- [ ] Test end-to-end workflows
- [ ] Performance testing (response times <500ms)
- **Assigned to:** Sai Charan Nagilla (Lead)  
- **Expected Start:** Mar 15, 2026

#### Security Testing
- [ ] Conduct security audit
- [ ] Test authentication/authorization mechanisms
- [ ] Validate data encryption (in-transit & at-rest)
- [ ] Penetration testing report
- **Assigned to:** Sandeep Reddy Manthena (Lead)  
- **Expected Start:** Mar 20, 2026

#### Bug Fixes & Optimization
- [ ] Fix identified issues
- [ ] Performance optimization
- [ ] Code refactoring
- [ ] Documentation update
- **Assigned to:** All team members  
- **Expected Completion:** Mar 31, 2026

---

### Phase 5: Final Delivery & Presentation (Apr 1-10, 2026) - NOT STARTED

#### Deployment
- [ ] Deploy to AWS (production environment)
- [ ] Configure CI/CD pipeline
- [ ] Set up monitoring and logging
- [ ] Create runbooks and documentation
- **Assigned to:** Pranav Dara (Lead), Sandeep Reddy Manthena  
- **Expected Start:** Apr 1, 2026

#### Final Deliverables
- [ ] Complete system documentation
- [ ] User guide and training materials
- [ ] Instructor presentation (≤10 minutes, all members participate)
- [ ] Individual contribution reports (each team member)
- [ ] Peer reviews (cross-team evaluations)
- **Assigned to:** All team members  
- **Due:** Apr 10, 2026

#### Quality Gate Review
- [ ] Code review and approval
- [ ] Documentation completeness check
- [ ] Final testing and validation
- [ ] Instructor sign-off
- **Assigned to:** Sai Charan Nagilla (Project Manager)

---

## 📅 SCHEDULE & MILESTONES

### Critical Path (6-Month Timeline)

```
Oct 10      Nov 1       Dec 1       Jan 1       Feb 1       Mar 1       Apr 10
  |           |           |           |           |           |           |
  └─PLANNING─┬─DESIGN───┬─DEVELOPMENT────────────┬─TESTING─┬─FINAL─────┘
            Oct 31    Nov 20                Mar 10 Mar 31   Apr 10
         Charter     Design Doc           Testing  Deploy   Present
```

### Milestone Timeline

| Milestone | Date | Status | Owner | Deliverables |
|-----------|------|--------|-------|--------------|
| **Team Formation & Kickoff** | Oct 10-20, 2025 | ✅ Completed | All | Team roster, communication plan |
| **Project Charter Approved** | Oct 21-31, 2025 | ✅ Completed | Sai Charan | Charter, financial analysis, risks |
| **System Design Complete** | Nov 1-20, 2025 | ✅ Completed | Pranav | Architecture docs, API specs |
| **GitHub Repository Ready** | Nov 23, 2025 | ✅ Completed | Sai Charan | 3 commits, all docs uploaded |
| **Sprint 1 AI Model (Baseline)** | Dec 5, 2025 | 🟡 60% | Sai Charan | Working classifier, feature extraction |
| **Sprint 2 Backend API** | Dec 20, 2025 | 🟡 50% | Pranav | Flask server, endpoints, database |
| **Sprint 3 Frontend UI** | Jan 20, 2026 | 🟡 40% | Sandeep | React components, UI/UX complete |
| **Sprint 4 Dashboard & Reports** | Feb 15, 2026 | 🟡 30% | Sai Charan | Risk visualization, reporting engine |
| **Testing & QA Complete** | Mar 31, 2026 | ⏳ Not Started | Pranav | >85% tests pass, <5 critical bugs |
| **Production Deployment** | Apr 5, 2026 | ⏳ Not Started | Pranav | Live on AWS, monitoring active |
| **Final Presentation** | Apr 8-10, 2026 | ⏳ Not Started | All | 10-min demo, Q&A, sign-off |

### Special Considerations
- **Ontario Family Day Holiday:** February 17, 2026 (no work scheduled)
- **Buffer Time:** 2 weeks built into testing phase for unexpected issues
- **Contingency:** Project can absorb 2-week delay while meeting Apr 10 deadline

---

## 📁 DOCS & FILES

### Repository Links
- **GitHub Repository:** https://github.com/saicharan714/Smart-Secure-Innovators_AI-Powered-Cybersecurity-Risk-Assessment-Portal
- **Branch:** main (3 commits, all pushed)

### Documentation Files (in `/docs`)
- ✅ `PROJECT_CHARTER.md` - Complete project specification
- ✅ `Cost_Calculations_Payback_NPV.md` - Financial analysis with verified metrics
- ✅ `Milestones_and_Schedule.md` - Detailed timeline
- ✅ `Updated_Project_Charter.pdf` - PDF version of charter
- ⏳ `BASECAMP_PROJECT_PLAN.md` - This document

### Code Files (in `/src`)
- ✅ `src/ai_model/vulnerability_classifier.py` - ML classifier
- ✅ `src/ai_model/evaluation/model_evaluator.py` - Model metrics
- ✅ `src/web_app/backend/app.py` - Flask REST API
- ✅ `src/web_app/frontend/package.json` - React configuration
- ✅ `src/dashboard/dashboard.py` - Risk dashboard module

### Test Files (in `/tests`)
- ✅ `tests/model_tests/test_classifier.py` - Unit tests for ML model
- ✅ `tests/api_tests/test_endpoints.py` - API endpoint tests
- ✅ `tests/ui_tests/test_components.py` - React component tests

### Support Documentation (root)
- ✅ `README.md` - Project overview and setup
- ✅ `API_DOCUMENTATION.md` - REST API reference
- ✅ `DEPLOYMENT_GUIDE.md` - Deployment instructions
- ✅ `LLM_ACKNOWLEDGMENT.md` - LLM usage disclosure
- ✅ `requirements.txt` - Python dependencies

---

## 👥 TEAM MEMBERS & RESPONSIBILITIES

### Sai Charan Nagilla
- **Role:** Project Manager, AI/ML Developer
- **Email:** saicharannagilla714@gmail.com
- **Responsibilities:**
  - Overall project management and coordination
  - AI model development (vulnerability classifier)
  - Dashboard and visualization module
  - GitHub repository management
- **Deliverables:** AI model, dashboard, project coordination

### Pranav Dara
- **Role:** System Architect, Backend Developer
- **Responsibilities:**
  - System architecture and design
  - Backend development (Flask API)
  - Database design and management
  - Testing and QA coordination
- **Deliverables:** Backend API, database, testing framework

### Sandeep Reddy Manthena
- **Role:** Frontend Developer, UI/UX Designer
- **Responsibilities:**
  - Frontend development (React)
  - User interface and user experience design
  - Security and authentication implementation
  - Deployment and DevOps
- **Deliverables:** Frontend application, security implementation, deployment

---

## 💰 BUDGET & RESOURCE ALLOCATION

### Budget Breakdown ($63,250 total)

| Category | Amount | Allocation |
|----------|--------|------------|
| **Labor** | $58,250 | 3 developers × 520 hrs × $37.47/hr |
| **Supplies & Tools** | $3,000 | Development tools, libraries, services |
| **Miscellaneous** | $2,000 | Infrastructure, contingency, miscellaneous |
| **TOTAL** | $63,250 | 100% |

### Resource Hours (per phase)
- **Phase 1 - Planning:** 40 hours (6.2%)
- **Phase 2 - Design:** 60 hours (9.2%)
- **Phase 3 - Development:** 320 hours (49.2%) ← CURRENT
- **Phase 4 - Testing:** 120 hours (18.5%)
- **Phase 5 - Final:** 60 hours (9.2%)
- **TOTAL:** 600 hours

### Resource Utilization
- **Current Week (Nov 23):** Phase 3 Development (50% resource allocation)
- **Next 2 Weeks:** Phase 3 Sprints 1-2 (100% resource allocation, 40 hours/person)
- **January-February:** Phase 3 Sprints 3-4 (100% resource allocation, 40 hours/person)

---

## 🎯 SUCCESS CRITERIA & KPIs

### Code Quality Metrics
- [ ] Code coverage: >85% of all modules
- [ ] Test pass rate: >90% of unit tests
- [ ] Code review: 100% of commits reviewed
- [ ] Cyclomatic complexity: <10 per function

### Performance Metrics
- [ ] API response time: <500ms (95th percentile)
- [ ] Model inference time: <2 seconds per prediction
- [ ] Dashboard load time: <2 seconds
- [ ] Uptime: >99.5%

### Project Delivery Metrics
- [x] Charter completed on time (Oct 31) ✅
- [x] Design completed on time (Nov 20) ✅
- [x] GitHub repository created with 3 commits (Nov 23) ✅
- [ ] Development completed on time (Mar 10)
- [ ] Testing completed on time (Mar 31)
- [ ] Final delivery on time (Apr 10)
- [ ] Budget adherence: ±10% of $63,250

### Business Metrics
- [x] Annual benefit: $65,000 ✅
- [x] Payback period: 0.97 years ✅
- [x] NPV: $104,270 ✅
- [x] ROI: 102.8% ✅

---

## 📊 CURRENT PROJECT STATUS (as of Nov 23, 2025)

**Overall Completion:** 50% (Documentation 8% + GitHub 4% = 12% of 25% final grade)

### Completed ✅
- Project Charter with full financial analysis
- System Design and Requirements
- GitHub Repository with 3 commits
- Initial codebase (skeleton/placeholders)
- API Documentation
- Deployment Guide

### In Progress 🔄
- Sprint 1: AI Model Development (60% - feature extraction pipeline)
- Sprint 2: Backend API (50% - routing and endpoints)
- Sprint 3: Frontend UI (40% - component structure)
- Sprint 4: Dashboard (30% - module skeleton)

### Not Started ⏳
- Sprint Testing Phase (Mar 11-31)
- Production Deployment (Apr 1-5)
- Final Presentation (<10 minutes, all members)
- Individual Contribution Reports (each member)
- Peer Reviews (cross-team evaluation)

---

## 🚀 NEXT ACTIONS (Priority Order)

### This Week (Nov 23-29, 2025)
1. Complete Sprint 1 AI Model training (target: >85% accuracy)
2. Create Product Roadmap document
3. Finalize presentation outline

### Next 2 Weeks (Nov 30 - Dec 13, 2025)
1. Complete Sprint 2 Backend API implementation
2. Begin Sprint 3 Frontend development
3. Develop presentation slides

### December 2025
1. Complete Sprint 3 Frontend UI
2. Begin Sprint 4 Dashboard implementation
3. Rehearse presentation with full team

### January-February 2026
1. Complete Sprint 4 Dashboard
2. Begin comprehensive testing
3. Prepare production deployment

### March 2026
1. Complete testing and bug fixes
2. Deploy to production
3. Finalize presentation

### April 2026
1. Final review and sign-off
2. Present to instructor (≤10 minutes)
3. Submit final deliverables

---

## 📞 COMMUNICATION & COLLABORATION

### Meeting Schedule
- **Weekly Standup:** Every Monday 10:00 AM (15 minutes)
- **Sprint Planning:** Every 2 weeks (1 hour)
- **Progress Review:** Every Friday 4:00 PM (30 minutes)
- **Ad-hoc:** As needed via Basecamp or GitHub

### Communication Channels
- **Basecamp:** Project planning, task tracking, file sharing
- **GitHub:** Code repository, pull requests, code reviews
- **Email:** Formal communications, external coordination

### Documentation Standards
- All commits must include descriptive messages
- Code must include docstrings and comments
- All features documented in README
- Changes logged in CHANGELOG

---

**Document Version:** 1.0  
**Last Updated:** November 23, 2025  
**Next Review:** December 7, 2025  
**Project Manager:** Sai Charan Nagilla
