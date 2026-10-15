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

- Pushing changes to the `qa` branch triggers the GitHub Actions workflow to validate the Python code, build a Docker image, publish it to GHCR, and deploy the image to the QA environment.
- Changes are promoted from `qa` to `main` through a pull request.
- Pushing the approved changes to `main` triggers the workflow to build and publish an image and deploy it to production.
- The deployment job depends on the successful build job, so deployment does not proceed if the build job fails.
- GitHub Actions secrets are used for deployment credentials. Secrets are not stored in the repository.

## Test Evidence

- **GitHub Actions:** https://github.com/BryanF23/self-hosted-site-is373/actions
- **Container image:** https://github.com/users/BryanF23/packages/container/package/self-hosted-site-is373
- **QA workflow run:** Add the direct link to a successful QA workflow run.
- **Production workflow run:** Add the direct link to a successful production workflow run.
- **Deployed image tag or commit:** Add the commit SHA/image tag used for the demonstrated deployment.
- **QA-to-production demonstration:** Add screenshots or a short recording showing the same visible change deployed to QA first and then production after promotion to `main`.
- **SSH security:** Add redacted evidence showing SSH access as the non-root user and the effective SSH settings disabling root and password login.

## Security

SSH access uses a non-root account and key-based authentication. Root SSH login and password-based SSH login are disabled. Deployment credentials are stored in GitHub Actions secrets.

**Never include private SSH keys, passwords, access tokens, or unredacted secrets in screenshots or repository files.**
