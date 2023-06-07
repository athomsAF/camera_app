# Transfer of video

## Websocket flux

```{mermaid}
sequenceDiagram

    Client->>Server: Connexion request
    Caamera->>Server: Get the flux of images
    Server->>Client: Send all image one by one (like mjpeg)
    Client->>Client: Display flux

```
:::{admonition} Attention au chemin d'accès
:class: attention
Bug during the reload of the page, the flux is not reloaded.
:::

## Explication of the code

```{eval-rst}
.. autofunction:: stream_socket_server.video_stream
```
test


<!-- ```{code-block} python
def check_if_commited() -> bool:
"""returns if the current branch is commited
Returns:
    bool: status of branch
"""
```

Vous pouvez utiliser la commande suivante:

```{code-block} markdown
\```{eval-rst}
.. autofunction:: noxfile.check_if_commited
\```
```

:::{admonition} Attention au chemin d'accès
:class: attention
Il faut spécifier à la place de noxfile le chemin d'accès jusqu'au fichier.
:::

:::{admonition} Auto-function!
:class: tip
We can also use automodule to auto-document a file
:::

Cela permet d'afficher le contenu de la manière suivante.



