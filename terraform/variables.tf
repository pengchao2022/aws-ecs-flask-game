variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "app_name" {
  description = "Application name"
  type        = string
  default     = "flask-to-do"
}

variable "environment" {
  description = "Environment name"
  type        = string
  default     = "production"
}

variable "github_repo" {
  description = "GitHub repository name"
  type        = string
}

variable "db_username" {
  description = "RDS master username"
  type        = string
  default     = "postgres"
}

variable "db_password" {
  description = "RDS master password"
  type        = string
  sensitive   = true
}