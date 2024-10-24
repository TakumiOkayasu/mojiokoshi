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

RUN curl -o ./create_user.sh https://raw.githubusercontent.com/TakumiOkayasu/shellscript_utility/refs/heads/main/create_user.sh \
    && curl -o ./terminal_config.sh https://raw.githubusercontent.com/TakumiOkayasu/shellscript_utility/refs/heads/main/terminal_config.sh \
    && chmod 777 ./*.sh \
    && ./create_user.sh \
    && ./terminal_config.sh\
    && rm *.sh

WORKDIR /workspace
USER ${USER_NAME}
SHELL ["/bin/bash", "-c"]
