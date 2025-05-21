# System Architecture

```mermaid
graph TD
    A[IoT Sensors] --> B(Cleaning Agent)
    B --> C{State Manager}
    C --> D[Action Dispatcher]
    D --> E[(Performance DB)]
```

## Components
1. **IoT Sensors** - Provide real-time home data
2. **Cleaning Agent** - Core decision-making logic
3. **State Manager** - Maintains system state
4. **Action Dispatcher** - Executes commands
5. **Performance DB** - Stores metrics and logs