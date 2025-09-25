terraform {
  backend "s3" {
    bucket         = "terraformstatefile090909"
    key            = "aws-ecs-flask-games.tfstate"
    region         = "us-east-1"
    dynamodb_table = "terraform-locks"
    encrypt        = true
  }
}                       