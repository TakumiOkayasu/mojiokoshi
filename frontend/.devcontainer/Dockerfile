FROM oven/bun:latest

# ヤケクソ
ENV USER_NAME ${USER_NAME} 
ENV USER_UID  ${USER_UID}
ENV USER_GID  ${USER_GID}

ARG USER_NAME ${USER_NAME}
ARG USER_UID  ${USER_UID}
ARG USER_GID  ${USER_GID}

RUN apt-get update && apt-get install -y --no-install-recommends \
    bash \
    curl \
    git \
    sudo \
    ssh \
    build-essential \
    ca-certificates \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /tmp/scripts/
COPY scripts .

RUN chmod 777 1_create_user.sh && chmod 777 2_terminal_config.sh \
    && ./1_create_user.sh \
    && ./2_terminal_config.sh

WORKDIR /workspace
USER ${USER_NAME}

