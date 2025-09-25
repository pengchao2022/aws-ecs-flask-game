output "alb_dns_name" {
  description = "ALB DNS 名称"
  value       = aws_lb.main.dns_name
}

output "ecr_repository_url" {
  description = "ECR 仓库 URL"
  value       = aws_ecr_repository.app.repository_url
}

output "db_endpoint" {
  description = "RDS 端点"
  value       = aws_db_instance.main.address
}

output "ecs_cluster_name" {
  description = "ECS 集群名称"
  value       = aws_ecs_cluster.main.name
}

output "ecs_service_name" {
  description = "ECS 服务名称"
  value       = aws_ecs_service.main.name
}