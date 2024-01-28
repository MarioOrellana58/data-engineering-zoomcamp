variable "project" {
  description = "Project"
  default     = "thinking-glass-412101"
}

variable "region" {
  description = "Project region"
  default     = "us-central1"
}

variable "credentials" {
  description = "Project credentials"
  default     = "./keys/my-creds.json"
}

variable "location" {
  description = "Project Location"
  default     = "US"
}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  default     = "demo_dataset"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  default     = "thinking-glass-412101-terra-bucket"
}

variable "gcs_storage_class" {
  description = "Bucket storage class"
  default     = "STANDARDS"
}