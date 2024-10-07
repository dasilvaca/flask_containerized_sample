from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from services.task_service import TaskService

task_blueprint = Blueprint("tasks", __name__)


@task_blueprint.route("/tasks", methods=["POST"])
def create_task():

    data = request.form
    name = data.get("name")
    description = data.get("description")

    if not name:
        return jsonify({"error": "Name is required"}), 400

    TaskService.create_task(name, description)
    return redirect(url_for("tasks.index"))


@task_blueprint.route("/edit_tasks", methods=["POST"])
def edit_task():
    data = request.form

    id = data.get("id")
    name = data.get("name")
    description = data.get("description")

    if not id:
        return jsonify({"error": "ID is required"}), 400
    if not name:
        return jsonify({"error": "Name is required"}), 400

    TaskService.edit_task(id, name, description)
    return redirect(url_for("tasks.edit_task_template"))


@task_blueprint.route("/")
def index():
    return render_template("index.html")

@task_blueprint.route("/edit_task")
def edit_task_template():
    return render_template("edit_task_template.html")