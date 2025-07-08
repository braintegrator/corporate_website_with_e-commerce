Project Rules for Corporate Website with E-commerce

Описание проекта

Проект представляет собой корпоративный веб-сайт с интегрированным интернет-магазином для компании, предоставляющей услуги, а также продающей товары. Интернет-магазин является составной частью сайта, но за его контент и функциональность отвечает Saleor, тогда как Wagtail CMS управляет контентом корпоративного сайта (страницы, блог, услуги). Сайт должен быть масштабируемым, SEO-оптимизированным, безопасным и поддерживать удобное управление контентом и заказами. Wagtail и Saleor взаимодействуют через GraphQL API для обеспечения единого доступа к данным.

Цели

Создать headless-архитектуру с разделением бэкенда (Django, Wagtail, Saleor) и фронтенда (Next.js).
Реализовать функционал интернет-магазина (каталог, корзина, оформление заказа, платежи, доставка) через Saleor.
Обеспечить управление контентом корпоративного сайта (страницы, блог, услуги) через Wagtail CMS.
Настроить взаимодействие между Wagtail и Saleor через GraphQL API.
Настроить CI/CD, мониторинг и логирование для поддержки проекта.

Технологический стек
Backend

Django: Основной фреймворк для веб-разработки.
Wagtail CMS: Headless CMS для управления контентом корпоративного сайта (страницы, блог, услуги).
Saleor: E-commerce платформа для управления контентом и функциональностью интернет-магазина (каталог, заказы, корзина) с GraphQL API.
PostgreSQL: Реляционная база данных.
Redis: Кэширование и брокер для Celery.
Celery: Асинхронные задачи.
Stripe: Платежная система.
EasyPost: Интеграция с FedEx и другими службами доставки.
GraphQL (Graphene-Django): API для взаимодействия фронтенда с Wagtail и Saleor.
Sentry: Мониторинг ошибок.
Flake8 + Black + isort: Линтинг и форматирование.
Pytest: Тестирование.
Docker: Контейнеризация.

Frontend

Next.js (14.x, App Router): Фреймворк для SSR/SSG и SEO.
TypeScript: Строгая типизация.
Tailwind CSS: Утилитарный CSS.
Chakra UI: UI-библиотека.
Apollo Client: GraphQL-запросы к Wagtail и Saleor.
NextAuth.js: Аутентификация.
Framer Motion: Анимации.
ESLint + Prettier: Линтинг и форматирование.
Cypress: E2E-тестирование.
Google Analytics 4: Аналитика.
Cloudinary: Оптимизация изображений.

Инфраструктура

GitHub Actions: CI/CD.
Vercel: Хостинг фронтенда.
DigitalOcean/AWS: Хостинг бэкенда.
Nginx: Реверс-прокси.
Prometheus + Grafana: Мониторинг.
Loki + Grafana: Логирование.

Архитектура

Headless-подход: Бэкенд (Django, Wagtail, Saleor) предоставляет данные через GraphQL API, фронтенд (Next.js) рендерит интерфейс.
Модульность: Wagtail управляет контентом сайта, Saleor — контентом и функциональностью интернет-магазина, изолированы в Django-приложениях.
API: GraphQL объединяет данные Wagtail (контент сайта) и Saleor (интернет-магазин) для фронтенда.
Асинхронность: Celery для задач (отправка писем, обработка заказов).
Контейнеризация: Docker для унификации разработки и продакшена.

Структура проекта
web_app/
├── backend/
│   ├── manage.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── web_app/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   ├── wagtail_app/
│   │   ├── models.py
│   │   ├── urls.py
│   ├── saleor_app/
│   │   ├── settings.py
│   │   ├── urls.py
│   └── tests/
├── frontend/
│   ├── package.json
│   ├── next.config.js
│   ├── app/
│   │   ├── layout.tsx
│   │   ├── page.tsx
│   ├── components/
│   │   ├── Header.tsx
│   │   ├── ProductCard.tsx
│   ├── lib/
│   │   ├── apollo-client.ts
│   ├── public/
│   └── cypress/
└── docker-compose.yml

Инструкции для ИИ-агента

Инициализация проекта:

Создать структуру папок согласно схеме выше, назвав корневую папку web_app.
Инициализировать Git-репозиторий с .gitignore для node_modules, venv, __pycache__.
Настроить Docker и docker-compose.yml для бэкенда, фронтенда, PostgreSQL и Redis.


Бэкенд:

Установить Django, Wagtail и Saleor в виртуальном окружении Python.
Настроить settings.py для подключения PostgreSQL, Redis, Celery, Stripe, EasyPost.
Создать приложения wagtail_app (контент сайта) и saleor_app (интернет-магазин) с изолированной логикой.
Реализовать GraphQL API через Graphene-Django, интегрировать Wagtail (контент сайта) и Saleor (интернет-магазин) для единого доступа через /graphql.
Настроить линтеры (Flake8, Black, isort) и тесты (Pytest).
Интегрировать Sentry для мониторинга.


Фронтенд:

Инициализировать Next.js с TypeScript, Tailwind CSS и App Router.
Установить Chakra UI, Apollo Client, NextAuth.js, Framer Motion.
Реализовать компоненты (Header, ProductCard) и страницы (каталог, корзина, страницы услуг).
Настроить GraphQL-запросы через Apollo Client к Wagtail (контент) и Saleor (магазин).
Интегрировать Google Analytics 4 и Cloudinary.
Настроить ESLint, Prettier и Cypress для тестирования.


Инфраструктура:

Настроить GitHub Actions для CI/CD (тесты, сборка, деплой).
Развернуть фронтенд на Vercel, бэкенд на DigitalOcean/AWS.
Настроить Nginx как реверс-прокси.
Интегрировать Prometheus, Grafana и Loki для мониторинга и логирования.


Тестирование и деплой:

Написать unit-тесты для бэкенда (Pytest) и E2E-тесты для фронтенда (Cypress).
Провести нагрузочное тестирование.
Выполнить деплой и проверить мониторинг через Sentry и Grafana.



Правила разработки

Следовать PEP 8 для Python и Airbnb-стандартам для TypeScript.
Использовать модульный подход: изолировать логику Wagtail (контент сайта) и Saleor (интернет-магазин).
Проверять код линтерами перед коммитами.
Писать тесты для всех критических функций (API, корзина, платежи).
Документировать API через GraphiQL.

Последовательность выполнения

Настройка окружения и инфраструктуры (Docker, CI/CD).
Разработка бэкенда: Django, Wagtail (контент), Saleor (интернет-магазин), GraphQL.
Разработка фронтенда: Next.js, Apollo Client, Chakra UI.
Интеграция бэкенда и фронтенда через GraphQL.
Тестирование, деплой и настройка мониторинга.


English Language
Project Description
The project is a corporate website with an integrated e-commerce store for a company providing services for smart home systems, as well as selling components for these systems. The e-commerce store is a component of the website, with Saleor managing its content and functionality, while Wagtail CMS handles the corporate website content (pages, blog, services). The site must be scalable, SEO-optimized, secure, and support easy content and order management. Wagtail and Saleor interact via a unified GraphQL API for seamless data access.
Objectives

Build a headless architecture with separated backend (Django, Wagtail, Saleor) and frontend (Next.js).
Implement e-commerce functionality (catalog, cart, checkout, payments, shipping) via Saleor.
Enable content management for the corporate website (pages, blog, services) via Wagtail CMS.
Configure interaction between Wagtail and Saleor through GraphQL API.
Set up CI/CD, monitoring, and logging for project maintenance.

Technology Stack
Backend

Django: Core web framework.
Wagtail CMS: Headless CMS for corporate website content (pages, blog, services).
Saleor: E-commerce platform for internet store content and functionality (catalog, orders, cart) with GraphQL API.
PostgreSQL: Relational database.
Redis: Caching and message broker for Celery.
Celery: Asynchronous tasks.
Stripe: Payment processing.
EasyPost: Integration with FedEx and other shipping services.
GraphQL (Graphene-Django): API for frontend interaction with Wagtail and Saleor.
Sentry: Error monitoring.
Flake8 + Black + isort: Linting and formatting.
Pytest: Testing.
Docker: Containerization.

Frontend

Next.js (14.x, App Router): Framework for SSR/SSG and SEO.
TypeScript: Strict typing.
Tailwind CSS: Utility-first CSS.
Chakra UI: UI component library.
Apollo Client: GraphQL queries to Wagtail and Saleor.
NextAuth.js: Authentication.
Framer Motion: Animations.
ESLint + Prettier: Linting and formatting.
Cypress: E2E testing.
Google Analytics 4: User analytics.
Cloudinary: Image optimization.

Infrastructure

GitHub Actions: CI/CD.
Vercel: Frontend hosting.
DigitalOcean/AWS: Backend hosting.
Nginx: Reverse proxy.
Prometheus + Grafana: Monitoring.
Loki + Grafana: Logging.

Architecture

Headless Approach: Backend (Django, Wagtail, Saleor) serves data via GraphQL API, frontend (Next.js) renders the UI.
Modularity: Wagtail manages website content, Saleor manages e-commerce content, isolated in Django apps.
API: GraphQL unifies data from Wagtail (website content) and Saleor (e-commerce) for the frontend.
Asynchronicity: Celery for tasks (emails, order processing).
Containerization: Docker for unified development and production.

Project Structure
web_app/
├── backend/
│   ├── manage.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── web_app/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   ├── wagtail_app/
│   │   ├── models.py
│   │   ├── urls.py
│   ├── saleor_app/
│   │   ├── settings.py
│   │   ├── urls.py
│   └── tests/
├── frontend/
│   ├── package.json
│   ├── next.config.js
│   ├── app/
│   │   ├── layout.tsx
│   │   ├── page.tsx
│   ├── components/
│   │   ├── Header.tsx
│   │   ├── ProductCard.tsx
│   ├── lib/
│   │   ├── apollo-client.ts
│   ├── public/
│   └── cypress/
└── docker-compose.yml

Instructions for AI Agent

Project Initialization:

Create the folder structure as shown above, naming the root folder web_app.
Initialize a Git repository with .gitignore for node_modules, venv, __pycache__.
Set up Docker and docker-compose.yml for backend, frontend, PostgreSQL, and Redis.


Backend:

Install Django, Wagtail, and Saleor in a Python virtual environment.
Configure settings.py for PostgreSQL, Redis, Celery, Stripe, EasyPost.
Create wagtail_app (website content) and saleor_app (e-commerce) with isolated logic.
Implement GraphQL API using Graphene-Django, integrating Wagtail (website content) and Saleor (e-commerce) for unified access via /graphql.
Set up linters (Flake8, Black, isort) and tests (Pytest).
Integrate Sentry for monitoring.


Frontend:

Initialize Next.js with TypeScript, Tailwind CSS, and App Router.
Install Chakra UI, Apollo Client, NextAuth.js, Framer Motion.
Implement components (Header, ProductCard) and pages (catalog, cart, service pages).
Configure GraphQL queries via Apollo Client to Wagtail (content) and Saleor (e-commerce).
Integrate Google Analytics 4 and Cloudinary.
Set up ESLint, Prettier, and Cypress for testing.


Infrastructure:

Configure GitHub Actions for CI/CD (tests, build, deploy).
Deploy frontend to Vercel, backend to DigitalOcean/AWS.
Set up Nginx as a reverse proxy.
Integrate Prometheus, Grafana, and Loki for monitoring and logging.


Testing and Deployment:

Write unit tests for backend (Pytest) and E2E tests for frontend (Cypress).
Perform load testing.
Deploy and verify monitoring via Sentry and Grafana.



Development Rules

Follow PEP 8 for Python and Airbnb standards for TypeScript.
Use a modular approach: isolate Wagtail (website content) and Saleor (e-commerce) logic.
Run linters before commits.
Write tests for critical features (API, cart, payments).
Document API via GraphiQL.

Execution Sequence

Set up environment and infrastructure (Docker, CI/CD).
Develop backend: Django, Wagtail (website content), Saleor (e-commerce), GraphQL.
Develop frontend: Next.js, Apollo Client, Chakra UI.
Integrate backend and frontend via GraphQL.
Test, deploy, and configure monitoring.


