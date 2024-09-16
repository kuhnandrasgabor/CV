### *Web based data management software*

The project was managed in Azure DevOps using a CI/CD pipeline implementation, hosted in Azure.
We decided on .Net Core with Blazor Razor pages, MongoDB for database and MAUI for Android and WebClient build targets.
The project was a complete rewrite of the existing software, with a focus on modularity and scalability, so we used 
a microservice architecture with a frontend server, core server, and various recognition module servers.

* SaaS software structure and design consultation for ERP software
* Azure cloud resource deployment and management
* Azure DevOps project management, CI/CD
* .Net Blazor Razor pages based project with MAUI multiplatform build targets
  * Azure bucket storage integration and management
  * API connections between
    * frontend server
    * core server
    * various recognition module servers
  * Image and Character recognition development and integration
  * Responsive UI with MudBlazor (although I'm not really a front-end developer)
  * ElasticSearch based page and usage analytics prototype
  * Media storage and streaming prototype with Azure media services
  * SAP integration prototype for SAP HANA S/4 Product Master Data