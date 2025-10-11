
***

# 🚀 DevOps Cloud Lab – Fullstack E-commerce Flask Demo



## 🌐 Overview

**DevOps Cloud Lab** is a complete cloud-native demonstration project.  
It showcases a modern DevOps workflow, utilizing continuous integration, automated testing, containerized deployment, and cloud infrastructure—all on a real, multi-page Flask e-commerce app.

- **Tech Stack:** Python (Flask), Docker, GitHub Actions, AWS EC2 (CentOS), Nginx, pytest
- **DevOps Features:** CI/CD, auto-deploy, logging, reverse proxy, infrastructure-as-code principles

***

## 📈 Live Demo

**Production URL:**  
[http://98.88.114.8/](http://98.88.114.8)

***

## 📦 Quick Links

- **DockerHub:** [priyanshuprafful](https://hub.docker.com/u/priyanshuprafful)
- **GitHub:** [priyanshuprafful/devops-cloud-lab](https://github.com/priyanshuprafful/devops-cloud-lab)
- **LinkedIn:** [Priyanshu Gupta](https://www.linkedin.com/in/priyanshu8787)

***

## 🛠️ Architecture

```
┌───────────┐
│  GitHub   │
└─────┬─────┘
      │  (push)
      ▼
┌────────────────┐
│GitHub Actions  │
│CI/CD Pipeline  │
└────────────────┘
      │
      ▼
┌──────────────────┐
│Docker Hub Repo   │
└──────────────────┘
      │
      ▼
┌──────────────┐
│AWS EC2 Server│
│(CentOS + Docker│
└─────┬────────┘
      │
      ▼
┌───────────┐
│ Flask App │
└─────┬─────┘
      │
      ▼
┌─────────┐
│ Nginx   │
└─────────┘
      │
      ▼
┌─────────────┐
│  End User   │
└─────────────┘
```

***

## 🧑‍💻 Features

**DevOps**
- End-to-end CI/CD with GitHub Actions (auto build, test, and deployment)
- Secure handling of credentials via GitHub Secrets
- Robust containerization: Docker image with dependencies baked in
- Fast rollback, repeatable deployments, and zero-downtime updates

**Cloud & Infra**
- AWS EC2 cloud server, auto-provisioned and Docker-ready
- Nginx reverse proxy for security, scalability, and forward compatibility (SSL ready)
- Port 80 public, Flask port protected—real production pattern

**App**
- Multi-page Flask e-commerce demo
- Attractive Bootstrap styling, dynamic routing
- Activity logging for every route/action
- Session-based cart and order flow

**Testing**
- Pytest-based automated tests for critical routes
- Tests enforced in pipeline (no deploy if tests fail)

***

## ✨ Usage & Deployment

### Clone & Run Locally
```bash
git clone https://github.com/priyanshuprafful/devops-cloud-lab.git
cd devops-cloud-lab
pip install -r requirements.txt
python app.py
```

### Docker Build & Run
```bash
docker build -t devops-cloud-lab .
docker run -d -p 5000:5000 devops-cloud-lab
```

### Access the app
Go to [http://localhost:5000](http://localhost:5000) (local) or [http://98.88.114.8](http://98.88.114.8) (cloud)

***

## 🤖 CI/CD Workflow Highlights

- **Trigger:** Every `push` to `main` branch
- **Steps:**
  1. Checkout repo code
  2. Install dependencies and run automated tests (pytest)
  3. Build Docker image, push to DockerHub
  4. SSH to EC2, pull updated image, restart container
  5. Auto-proxy via Nginx on port 80

**Config file:** `.github/workflows/docker-image.yml`

***

## 📢 Endpoints

| Route      | Description           |
|------------|----------------------|
| `/`        | Home page            |
| `/products`| List products        |
| `/cart`    | View cart            |
| `/order`   | Place order summary  |

***

## 📚 Documentation

- **Project structure, pipeline design, cloud setup, and deployment steps fully documented**
- **Detailed comments in workflow YAML and Flask code**
- **For complete stepwise guide, see the [Wiki](#) or Issues Tab**

***

## ⚡ Credits

- Developed by [Priyanshu Gupta](https://www.linkedin.com/in/priyanshu8787)
- Dev guidance and troubleshooting powered by [Perplexity AI](https://perplexity.ai/)

***

## 💡 Contact & Connect

- **LinkedIn:** [Priyanshu Gupta](https://www.linkedin.com/in/priyanshu8787)
- **GitHub:** [priyanshuprafful](https://github.com/priyanshuprafful)
- **Portfolio:** [priyanshuprafful.netlify.app](https://priyanshuprafful.netlify.app/)

***

**Want to collaborate, suggest a feature, or hire? Just connect above!**

***

**Paste this in your repo's `README.md`. Recruiters, interviewers, and teammates will get a crystal-clear view of your work and skills!**
If you want more tips, markdown tweaks, or architecture image, just ask!

[1](https://github.com/priyanshuprafful)