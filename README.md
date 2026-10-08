# Bryan's Self-Hosted Site

- **Production:** [http://bryanfselfhosted.xyz](http://bryanfselfhosted.xyz)
- **QA:** qa.bryanfselfhosted.xyz

Runs on a DigitalOcean Droplet with Flask, Docker, PostgreSQL, and Traefik.

## Test Evidence

- **QA workflow run:** Add link after a successful run.
- **Production workflow run:** Add link after a successful run.
- **Image registry:** Add registry link and deployed image tag or commit.
- **QA then production:** Add screenshots or a short recording showing the same visible change in QA and then production.
- **SSH security:** Add redacted evidence of SSH-key login as the non-root user and effective settings disabling root and password login. Never include passwords, tokens, or private keys.

## CI/CD and promotion

Document which branch deploys to QA and which promotion deploys to production, what validation runs, how the image is built and pushed, and how deployment reaches the Droplet.
