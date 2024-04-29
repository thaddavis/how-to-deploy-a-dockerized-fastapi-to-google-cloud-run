# Part 3

## Follow along

1. Open the `Dockerfile.dev` file
2. Go to VSCode Command Palette (ie: SHIFT + CMD + P)
    - Select `Developer: Reload Window`
3. Rebuild the "Dev Container"
4. SMOKE TEST the "Dev Container"
    - `gcloud --version` -> 473.0.0
5. "Create a Project" in your GCP account
6. `gcloud init`
    - ie: Paste the Verification Code into your Terminal
7. Enable the `Artifact Registry API` on your GCP project
8. `gcloud artifacts repositories create custom-fastapi --repository-format docker --project h-t-d-a-f-a-t-g-c-r --location us-central1`
9. `touch Dockerfile.prod`
10. `touch cloudbuild.yaml`
11. `gcloud builds submit --config=cloudbuild.yaml --project h-t-d-a-f-a-t-g-c-r .`
12. Check the GCP console after submitting the build: https://console.cloud.google.com/artifacts
13. `touch service.yaml`
14. `gcloud run services replace service.yaml --region us-east1`
15. `touch gcr-service-policy.yaml`
16. `gcloud run services set-iam-policy custom-fastapi-service gcr-service-policy.yaml --region us-east1`

## Reference links

- https://fastapi.tiangolo.com/
- https://cloud.google.com/run
- https://cloud.google.com/sdk/gcloud
- https://cloud.google.com/run/docs/deploying
