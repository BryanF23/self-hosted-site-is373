# Bryan's Self-Hosted Site

## Live Websites

- **Production:** https://bryanfselfhosted.xyz
- **QA:** https://qa.bryanfselfhosted.xyz

This project runs on a DigitalOcean Droplet using Flask, Docker, PostgreSQL, and Traefik. Traefik handles HTTPS for both environments.

## Architecture

- **Application:** Flask and Python
- **Containers:** Docker and Docker Compose
- **Database:** PostgreSQL, with separate production and QA databases
- **HTTPS and routing:** Traefik
- **Container registry:** GitHub Container Registry (GHCR)
- **CI/CD:** GitHub Actions

## CI/CD and Branch Promotion

- Pushing changes to `qa` triggers Python syntax validation, Docker image building, publishing to GHCR, and QA deployment.
- Changes are promoted from `qa` to `main` through a pull request.
- Pushing approved changes to `main` triggers the production build and deployment.
- The deployment job runs only after the build job succeeds.
- Deployment credentials are stored in GitHub Actions secrets.

## Test Evidence

- **GitHub Actions:** https://github.com/BryanF23/self-hosted-site-is373/actions
- **Container image:** https://github.com/users/BryanF23/packages/container/package/self-hosted-site-is373
- **QA workflow runs:** https://github.com/BryanF23/self-hosted-site-is373/actions?query=branch%3Aqa
- **Production workflow runs:** https://github.com/BryanF23/self-hosted-site-is373/actions?query=branch%3Amain
- **Deployed image tag or commit:** See the successful workflow run for the commit SHA used for deployment.
- **QA-to-production demonstration:** [QA website screenshot](evidence/qa-website-page-1.png) and [Production website screenshot](evidence/production-website-page-1.png).
- **SSH security:** [Non-root SSH login screenshot](evidence/ssh-non-root-login.png). Additional redacted evidence of the effective SSH settings should be included.

## Security

SSH access uses a non-root account and key-based authentication. Root SSH login and password-based SSH login are disabled. Deployment credentials are stored in GitHub Actions secrets.

Never include private SSH keys, passwords, or access tokens in the repository.