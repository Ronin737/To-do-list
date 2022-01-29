Application:-
 A simple to-do listing backend API using django. Tasks can be added with details like name, description and the date and time for doing. Each task added has details like challenges, time to complete and progress percent.
Tasks can be pinned if they are used regularly. Once marked complete, unpinned tasks get removed fro the database. Pinned tasks get their status changed to 'Complete' when marked finished.
Pinned tasks can also be restarted with fresh details.
All task related fields can be updated except status, which can only be marked complete or incomplete.
Any task can be deleted regardless of whether they are pinned or not.

API endpoints:-
1. For listing all tasks
2. For creating a new task
3. For listing all pinned tasks
4. For listing all completed tasks(Since all unpinned tasks are removed on completion, all completed tasks are pinned tasks)
5. For listing all incomplete tasks
6. For displaying details of any selected task
7. For updating details of any selected task
8. For deleting any selected task
9. For marking any task as complete. Unpinned tasks are removed from database on completion, while pinned tasks have their status changed to complete.
10. For restarting any pinned task that is completed.

All dependencies specified in requirements.txt.
