variable "aws_region" {
  description = "AWS 区域"
  type        = string
  default     = "us-east-1"
}

variable "app_name" {
  description = "应用名称"
  type        = string
  default     = "flask-game"
}

variable "environment" {
  description = "环境名称"
  type        = string
  default     = "production"
}

variable "db_username" {
  description = "RDS 用户名"
  type        = string
  sensitive   = true
}

variable "db_password" {
  description = "RDS 密码"
  type        = string
  sensitive   = true
}

variable "github_repo" {
  description = "GitHub 仓库名称"
  type        = string
}