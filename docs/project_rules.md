Правила проекта для Trae AI (Проект: Корпоративный сайт с интернет-магазином)
Эти правила специфичны для проекта "Корпоративный сайт с интернет-магазином" и должны строго соблюдаться.

1. Стек технологий

Backend: Python с Django, Wagtail CMS (для контента сайта), Saleor (для контента и функциональности интернет-магазина).
Frontend: Next.js (14.x, App Router) с TypeScript.
База данных: PostgreSQL.
Кэширование и брокер сообщений: Redis.
Асинхронные задачи: Celery.
Платежи: Stripe.
Доставка: EasyPost (интеграция с FedEx и другими службами).
API: GraphQL (Graphene-Django) для взаимодействия Wagtail и Saleor с фронтендом.
Хостинг: Vercel (фронтенд), DigitalOcean/AWS (бэкенд и база данных).
Контейнеризация: Docker.
CI/CD: GitHub Actions.
Мониторинг: Sentry (ошибки), Prometheus + Grafana (производительность), Loki + Grafana (логирование).
Стили: Tailwind CSS, Chakra UI.
Анимации: Framer Motion.
Аналитика: Google Analytics 4.
Оптимизация изображений: Cloudinary.
Аутентификация: NextAuth.js (JWT, OAuth), Saleor JWT.
Тестирование: Pytest (бэкенд), Cypress (фронтенд).
Линтинг: Flake8, Black, isort (бэкенд), ESLint, Prettier (фронтенд).

2. Соглашения по именованию

Модели Django: Имена классов в PascalCase (например, HomePage, ProductCategory).
API Endpoints: Используй kebab-case для URL-путей (например, /graphql, /api/wagtail/pages, /api/saleor/products).
Компоненты Next.js: Имена файлов и компонентов в PascalCase (например, ProductCard.tsx, ServicePage.tsx).
Переменные и функции в JavaScript/TypeScript: Используй camelCase (например, fetchProducts, productData).
GraphQL-запросы: Имена запросов в camelCase (например, getProductList, fetchPageContent).

3. Обработка ошибок

Все ошибки API должны возвращать стандартный JSON-объект с полями code, message и details (если применимо). Например: {"code": 400, "message": "Invalid product ID", "details": "Product ID must be a positive integer"}.
Используй Sentry для логирования всех критических ошибок на сервере. Уровень логирования: ERROR.
Логируй клиентские ошибки через Sentry Browser SDK (для фронтенда).

4. Тестирование

Для каждой новой фичи обязательно напиши unit-тесты с покрытием не менее 80% (используй Pytest с pytest-cov для бэкенда).
Пиши E2E-тесты для критических сценариев (корзина, оформление заказа, просмотр страниц) с использованием Cypress.
Используй factory-boy для создания тестовых данных в Django.
Тестируй GraphQL-запросы к Wagtail и Saleor отдельно.

5. Коммиты и ветки

Используй Conventional Commits. Пример: feat: добавить страницу каталога товаров в Saleor, fix: исправить ошибку в GraphQL-запросе.
Работай в отдельных ветках для каждой задачи (например, feature/product-catalog, bugfix/cart-checkout, hotfix/auth-error).
Ветка main всегда должна быть стабильной и готовой к деплою.

6. Принципы безопасности

Никогда не хардкодь учетные данные. Используй переменные окружения (.env) для ключей API (Stripe, EasyPost, Sentry) и настроек базы данных.
Проверяй все пользовательские вводы для предотвращения SQL-инъекций, XSS и CSRF-атак (используй встроенные механизмы Django и Next.js).
Валидируй и санируй весь пользовательский ввод:
На бэкенде: используй сериализаторы Graphene-Django и встроенные проверки Saleor/Wagtail.
На фронтенде: используй библиотеки вроде DOMPurify для защиты от XSS.


Настрой CORS для ограничения доступа к GraphQL API только с домена фронтенда.
Используй HTTPS (Let’s Encrypt) для всех продакшен-деплоев.

