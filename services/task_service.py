from repositories.task_repository import TaskRepository

class TaskService:

    @staticmethod
    def create_task(name, description):
        return TaskRepository.create_task(name, description)
    
    @staticmethod
    def edit_task(id, name, description):
        return TaskRepository.edit_task(id, name, description)