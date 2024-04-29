# Part 4

## Follow along

1. `mkdir -p .github/workflows`
2. `touch .github/workflows/cicd.yaml`
3. trigger an action by pushing to your `main` branch
4. View the status of the "action" in real-time on the Actions tab

## Reference links

- https://dev.to/rushi-patel/deploy-next-js-app-to-google-cloud-run-with-github-actions-cicd-a-complete-guide-l29

## Troubleshooting

If you run permissions issues with your Google Service Account then try these commands...

```.sh
gcloud projects add-iam-policy-binding h-t-d-a-f-a-t-g-c-r \
    --member="serviceAccount:htddfatgcr@h-t-d-a-f-a-t-g-c-r.iam.gserviceaccount.com" \
    --role="roles/artifactregistry.writer"

gcloud projects add-iam-policy-binding h-t-d-a-f-a-t-g-c-r \
  --member="serviceAccount:htddfatgcr@h-t-d-a-f-a-t-g-c-r.iam.gserviceaccount.com" \
  --role="roles/run.admin"

gcloud projects add-iam-policy-binding h-t-d-a-f-a-t-g-c-r \
  --member="serviceAccount:htddfatgcr@h-t-d-a-f-a-t-g-c-r.iam.gserviceaccount.com" \
  --role="roles/iam.serviceAccountUser"
  ```
