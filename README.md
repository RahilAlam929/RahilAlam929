# Hi, I'm MD Rahil

** Software Engineer · AI/ML Enthusiast · Open-Source Contributor**

I build full-stack systems, developer tools, and automation workflows with a focus on backend architecture, code intelligence, and practical ML integration. My work spans REST API design, static analysis tooling, ML pipelines, and CI/CD automation.

---

## Currently Building

- Code intelligence and static analysis platforms
- ML pipelines for real-world classification problems
- Full-stack applications with Next.js and FastAPI
- Reusable GitHub Actions for repository automation
- Open-source developer tools and infrastructure

---

## Tech Stack

**Languages**
`Python` `TypeScript` `JavaScript` `Java`

**Frontend**
`Next.js` `React` `Tailwind CSS`

**Backend**
`FastAPI` `Spring Boot` `Node.js`

**Databases**
`PostgreSQL` `SQLite` `Prisma` `Alembic`

**AI / ML**
`scikit-learn` `Pandas` `NumPy`

**DevOps & Infrastructure**
`Docker` `GitHub Actions` `Bash` `Linux`

---

## Featured Projects

### [DevAnalyzeX](https://github.com/RahilAlam929/DevAnalyzeX)

Full-stack static analysis platform that detects code quality, security, and maintainability issues across a repository via a REST API and Next.js dashboard.

`Python` `FastAPI` `Next.js` `PostgreSQL` `Alembic` `Docker`

- Asynchronous scan execution via FastAPI `BackgroundTasks` with lifecycle tracking (`pending → running → completed`)
- Regex-based static analysis across 14 file extensions; findings bucketed by severity (`high / medium / low / info`)
- JWT authentication with HttpOnly cookies and Argon2 password hashing; user-scoped access enforced at every layer
- PostgreSQL schema managed via Alembic migrations; full Docker Compose service stack

---

### [FraudGuard AI](https://github.com/RahilAlam929/fraudguard-ai)

End-to-end ML pipeline and REST API for credit card fraud detection on a severely imbalanced dataset (0.17% fraud rate).

`Python` `scikit-learn` `FastAPI` `Pydantic` `Pandas`

- Trains Logistic Regression and Random Forest classifiers with `class_weight="balanced"` to address class imbalance
- Evaluated on PR-AUC, F1, and confusion matrix — metrics meaningful under severe imbalance
- FastAPI inference service: accepts raw transaction data, applies saved scaler, returns fraud probability and three-tier risk level (`LOW / MEDIUM / HIGH`)
- Includes threshold analysis for precision/recall trade-off exploration and automated API test suite

---

### [StudentOS](https://github.com/RahilAlam929/StudentOs)

Full-stack student lifecycle platform unifying academic tracking, project management, internship pipelines, and career planning in a single authenticated workspace.

`Java` `Spring Boot` `Next.js` `PostgreSQL` `Docker Compose` `GitHub Actions`

- Spring Boot backend following controller → service → repository architecture with JWT-based authentication
- Swappable AI provider layer (OpenAI, Gemini, or local mock) configured via environment variables
- Docker Compose for local development; GitHub Actions CI pipeline for automated builds
- PostgreSQL data model covering the full student lifecycle as a single connected domain

---

### [BLOGVERSE](https://github.com/RahilAlam929/BLOGVERSE)

Multi-user blogging platform with image upload, a public content feed, and author-scoped post management.

`Next.js` `TypeScript` `Prisma` `PostgreSQL` `Cloudinary` `Tailwind CSS`

- Next.js App Router with TypeScript; Prisma ORM managing PostgreSQL schema and queries
- Cloudinary integration for blog image storage and delivery
- Author-only edit/delete access control enforced at the backend layer
- Deployed at [blogverse-navy.vercel.app](https://blogverse-navy.vercel.app)

---

### [RuntimeLens](https://github.com/RahilAlam929/RuntimeLens)

Developer tool for uploading a project, exploring source files, and running automated static review in a single workspace.

`Next.js` `TypeScript` `Prisma` `SQLite`

- Single-workspace interface replacing the need to switch between editor, terminal, and separate analysis tools
- File tree navigation and source code inspection across uploaded projects
- Automated review pipeline surfacing potential issues before production
- Prisma + SQLite for local project and findings persistence

---

### [repo-health-action](https://github.com/RahilAlam929/repo-health-action)

Reusable GitHub Action that checks repository health and outputs a score and grade — published on the GitHub Marketplace.

`GitHub Actions` `Bash` `YAML`

- Checks four dimensions: README, LICENSE, GitHub Actions configuration, and minimum file presence
- Outputs `health-score` (0–100) and `grade` as step outputs consumable by downstream workflow steps
- Configurable minimum score gate for enforcing quality standards on push or pull request

---

## Open Source

| Project | Description |
|---|---|
| [developer-roadmap](https://github.com/nilbuild/developer-roadmap) | Community-maintained developer learning roadmaps — contributed to roadmap content |
| [kana-dojo](https://github.com/lingdojo/kana-dojo) | Japanese learning platform built with Next.js — contributed to content and i18n |
| [open-elements-website](https://github.com/OpenElements/open-elements-website) | OpenElements web presence — contributed to site maintenance and configuration |
| [firstcontributions](https://github.com/firstcontributions/firstcontributions.github.io) | Open-source onboarding platform for first-time contributors |

---

## Engineering Focus

Areas I actively work in and explore:

Full-Stack Engineering · Backend Systems · REST API Design · AI/ML Pipelines · Static Analysis · Code Intelligence · GitHub Automation · CI/CD · Security Fundamentals · Open Source

---

## GitHub Stats

<div align="center">

<img src="./github-stats.svg" height="195"/>
&nbsp;&nbsp;
<img src="./top-langs.svg" height="195"/>

</div>

---

## Connect

[![GitHub](https://img.shields.io/badge/GitHub-RahilAlam929-181717?style=flat-square&logo=github)](https://github.com/RahilAlam929)
&nbsp;
[![LinkedIn](https://img.shields.io/badge/LinkedIn-MD%20Rahil-0A66C2?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/md-rahil-a070b3329/)

---

<sub>Build. Ship. Learn. Contribute.</sub>
