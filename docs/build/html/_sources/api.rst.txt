.. _api_reference:

API Reference
=============

Diese Dokumentation beschreibt die verschiedenen Komponenten der Projekt-API,
organisiert nach Django-Apps.

Join App (`join_app`)
----------------------

Diese App beinhaltet die Kernlogik für Tasks, Kontakte usw.

**Models:**

.. automodule:: join_app.models
   :members:
   :undoc-members:
   :show-inheritance:

**Serializers:**

.. automodule:: join_app.api.serializers
   :members:
   :undoc-members:
   :show-inheritance:

**Views:**

.. automodule:: join_app.api.views
   :members:
   :undoc-members:
   :show-inheritance:


User Authentication App (`user_auth_app`)
-----------------------------------------

Diese App ist verantwortlich für Benutzerregistrierung, Login und Profile.

**Models:**

.. automodule:: user_auth_app.models
   :members:
   :undoc-members:
   :show-inheritance:

**Serializers:**

.. automodule:: user_auth_app.api.serializers
   :members:
   :undoc-members:
   :show-inheritance:

**Views:**

.. automodule:: user_auth_app.api.views
   :members:
   :undoc-members:
   :show-inheritance: