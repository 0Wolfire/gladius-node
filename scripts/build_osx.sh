#!/usr/bin/env bash
#
# Build all mac binaries

LDFLAGS="" TARGET=/build/gladius SOURCE=/src/gladius-cli/cmd/main.go PROJECT_ROOT=/src/gladius-cli /scripts/go_osx.sh
LDFLAGS="" TARGET=/build/gladius-edged SOURCE=/src/gladius-edged/cmd/gladius-edged/main.go PROJECT_ROOT=/src/gladius-edged /scripts/go_osx.sh
LDFLAGS="" TARGET=/build/gladius-network-gateway SOURCE=/src/gladius-network-gateway/cmd/main.go PROJECT_ROOT=/src/gladius-network-gateway /scripts/go_osx.sh
LDFLAGS="" TARGET=/build/gladius-guardian SOURCE=/src/gladius-guardian/main.go PROJECT_ROOT=/src/gladius-guardian /scripts/go_osx.sh
