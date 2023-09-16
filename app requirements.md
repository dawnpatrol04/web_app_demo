 
## FastAPI + HTMX Web App with Highcharts Integration

#### Overview

This web app leverages FastAPI for the backend and HTMX for frontend dynamic content, with Highcharts for advanced charting capabilities. The design theme focuses on a minimalist aesthetic with mostly white, accented by black and red elements, styled with TailwindCSS. Given the constraints of operating behind a proxy, all external assets, including those from CDNs, will be hosted locally.

#### App Technology Stack:

- **Modular Development**: Build and test components in isolation to ensure reusability and maintainability. Tools like Storybook can help visualize components in a standalone environment.

- **HTMX**: Employ HTMX attributes on HTML elements to instill dynamism, such as loading data into a component without refreshing the entire page.

- **Highcharts**: To avoid external dependencies, download the Highcharts library and host it within the `/static/js` directory. Then, refer to this local version in your templates.

- **FastAPI**: Leverage FastAPI's dependency injection system to maintain clean route handlers. Furthermore, utilize Pydantic models for data validation and serialization.

- **Testing**: Prioritize writing tests for routes and services. FastAPI's `TestClient` streamlines this process.

- **Authentication**: For authentication integrations, harness FastAPI's security utilities. Combine these with a library like `python-jose` for JWT tokens.

#### PAGES
- Home / index ( just kind of a landing page with some info and links to other pages)
- Apps: Goes to a page with a group of Cards that link to the different apps)
- News: Goes to a page with a group of Cards that link to the different newsletters ( there will probably just be other pages for now))
- Learn: Goes to a page with a group of training and other resources Using Cards)
- About: Talks about our team and the projects)


#### App Layout
#####  Header 
 - logo to the left User icon to the right, when clicked it will drop down a menu with the following options
   - Profile
   - Settings
   - Logout
- Nav Bar
  - this will be a horizontal bar that will have the following links
    - Home
    - Apps
    - News
    - Learn
    - About
- Main Content
  - this will be the main content of the page and will change depending on the page
- Footer
  - this is the footer and will be minimalistic 


## FastAPI + HTMX Web App File Structure

```markdown
/myapp
|-- /app
|   |-- /main
|   |   |-- __init__.py
|   |   |-- routes.py       # Defines routes and their handlers
|   |   |-- models.py       # Data models (if using an ORM like SQLAlchemy)
|   |   |-- services.py     # Business logic and data services
|   |   |-- /templates
|   |   |   |-- base.html   # Base layout with navbar, sidebar, and main content section
|   |   |   |-- homepage.html   # Main content of the homepage
|   |   |   |-- /components
|   |   |   |   |-- card.html   # Reusable KPI card component
|   |   |   |   |-- graph.html  # Reusable graph component
|   |   |-- /static
|   |   |   |-- /css        # Stylesheets
|   |   |   |-- /js         # JavaScript files (if any)
|   |   |   |-- /images     # Images and icons
|   |-- /database           # Database configurations and migrations
|   |-- /auth               # Authentication functions and configurations
|   |-- /utils              # Helper functions and utility scripts
|   |-- /middlewares        # Middlewares for request/response processing
|-- /tests                  # Unit and integration tests
|   |-- /unit               # Unit tests
|   |-- /integration        # Integration tests
|-- main.py                 # Main entry point for the FastAPI app
|-- requirements.txt        # List of Python packages required
|-- config.py               # Global configuration settings
|-- alembic.ini             # Alembic (or another tool) config for database migrations
|-- README.md               # Documentation for setting up, running, and using the app
|-- .gitignore              # Specifies intentionally untracked files to ignore in Git
|-- Dockerfile              # Instructions for Docker containerization (if you plan to use Docker)
|-- docker-compose.yml      # Defines and runs multi-container Docker applications (if relevant)
|-- .env                    # Environment variables, ensure it's gitignored for security
```


#### Theme and Styling

- **TailwindCSS**: TailwindCSS is a utility-first CSS framework that allows for rapid styling of components. It is highly customizable and can be configured to purge unused styles, resulting in a smaller CSS file. This is especially useful for production environments.
- **Color / Theme**: The theme will be mostly white, with black and red accents. The color palette will be limited to a few colors to maintain a minimalist aesthetic. The color palette will be defined in the `tailwind.config.js` file.
- **light / dark mode**: The app will support both light and dark mode. This will be implemented using TailwindCSS's `@apply` directive to apply a different color scheme to the same component, depending on the mode. The mode will be toggled by a button in the navbar.

