# =============================================================================
"""Training Hyperparameters"""
# =============================================================================

xl_args = {"train_batch_size": 12, "learning_rate": 2e-05, "logging_steps": 50,
           "max_grad_norm": 1.0, "n_gpu": 1, "num_train_epochs": 2, "optimizer": "AdamW",
           "overwrite_output_dir": True, "adam_epsilon": 1e-08, "polynomial_decay_schedule_lr_end": 1e-07,
           "polynomial_decay_schedule_power": 1.0, "save_model_every_epoch": True,
           "save_optimizer_and_scheduler": True, "save_steps": -1, "scheduler": "linear_schedule_with_warmup",
           "use_multiprocessing": False, "warmup_steps": 8344, "model_class": "ClassificationModel",
           "labels_list": ["machine", "human"], "labels_map": {"machine": 0, "human": 1}}

db_args = {"train_batch_size": 16, "learning_rate": 1e-05, "logging_steps": 50,
           "max_grad_norm": 1.0, "n_gpu": 1, "num_train_epochs": 2, "optimizer": "AdamW",
           "overwrite_output_dir": True, "adam_epsilon": 1e-08, "polynomial_decay_schedule_lr_end": 1e-07,
           "polynomial_decay_schedule_power": 1.0, "save_model_every_epoch": True,
           "save_optimizer_and_scheduler": True, "save_steps": -1, "scheduler": "linear_schedule_with_warmup",
           "use_multiprocessing": False, "warmup_steps": 25000, "model_class": "ClassificationModel",
           "labels_list": ["machine", "human"], "labels_map": {"machine": 0, "human": 1}}