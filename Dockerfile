FROM python:3.10-slim AS base

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends curl git build-essential python3-setuptools \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/apt/lists/* \
    && rm -rf /var/cache/apt/*

FROM base AS base-prod

WORKDIR /app
COPY . ./

RUN pip install --only-root

# create a non-root user and switch to it, for security.
RUN addgroup --system --gid 1001 "app-user"
RUN adduser --system --uid 1001 "app-user"
USER "app-user"

ENTRYPOINT ["/bin/sh", "-c"]
CMD ["./scripts/entry"]