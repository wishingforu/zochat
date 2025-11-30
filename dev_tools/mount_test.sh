#!/bin/bash
# Simplified mount command that ACTUALLY WORKS

# Kill existing servers
pkill -f "python.*zoMount" 2>/dev/null

# Start server
echo "Starting server..."
py -u zoMount > "$TEMP/zoMount.log" 2>&1 &

# Wait for it
sleep 5

# Get port
PORT=$(grep -o "localhost:[0-9]*" "$TEMP/zoMount.log" | grep -o "[0-9]*" | head -1)

if [ -z "$PORT" ]; then
    PORT=9999
fi

echo "Server on port: $PORT"

# Mount
net use Z: /delete /y 2>/dev/null
net use Z: "http://127.0.0.1:$PORT" /user:dummy dummy

if [ $? -eq 0 ]; then
    echo "SUCCESS - Z: mounted"
    ls Z: 2>/dev/null | head -5
else
    echo "FAILED to mount"
    exit 1
fi
