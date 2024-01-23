terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.13.0"
    }
  }
}

provider "google" {
  project = "thinking-glass-412101"
  region  = "us-central1"
  credentials = "./keys/my-creds.json"
}

resource "google_storage_bucket" "demo-bucket" {
  name          = "thinking-glass-412101-terra-bucket"
  location      = "US"
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}