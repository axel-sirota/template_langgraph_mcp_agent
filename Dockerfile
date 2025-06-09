# builder image
FROM python:3.12-slim AS builder
WORKDIR /app
COPY pyproject.toml .
RUN pip install --no-cache-dir hatchling

# runtime image
FROM python:3.12-slim
WORKDIR /app
COPY --from=builder /usr/local/lib/python*/dist-packages /usr/local/lib/python*/dist-packages
COPY . .
RUN useradd -m appuser && chown -R appuser /app
USER appuser
CMD ["python", "-m", "{{cookiecutter.project_slug}}.main"]
