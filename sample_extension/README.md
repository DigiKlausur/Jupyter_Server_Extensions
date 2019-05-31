## Jupyter Server Extensions

This FAQ describes how to create a jupyter server extension using anaconda environments.

First create a new environment with:

```conda create -n my_env jupyter```

Activate it:

```conda activate my_env```

The sample extension is located in my_package.
To install it, navigate to the folder my_package and install via:

```pip install -e .```

Then navigate to the folder:

```anaconda3/envs/my_env/etc/jupyter```

and copy the file ***jupyter_notebook_config.json*** to it.

Now the extension will be loaded everytime you start the jupyter notebook server.

