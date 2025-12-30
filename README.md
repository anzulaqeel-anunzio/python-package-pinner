# Package.json Version Pinner Checker

A CLI tool that enforces strict versioning in `package.json` files. It ensures dependencies do not use ranges (like `^1.0.0` or `~2.3`) to prevent "it works on my machine" issues caused by unexpected minor/patch updates.

<!-- Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742 -->

## Features

*   **Strict Checks**: Flags any version using `^`, `~`, `>`, `<`, `*` or `latest`.
*   **Comprehensive**: Checks `dependencies`, `devDependencies`, `peerDependencies`, and `optionalDependencies`.
*   **Zero Dependencies**: Uses Python's built-in JSON parser.

## Usage

```bash
python run_checker.py [path]
```

### Examples

**1. Scan Project**
```bash
python run_checker.py
```

**2. Check Specific File**
```bash
python run_checker.py package.json
```

## Requirements

*   Python 3.x

## Contributing

Developed for Anunzio International by Anzul Aqeel.
Contact: +971545822608 or +971585515742

## License

MIT License. See [LICENSE](LICENSE) for details.


---
### 🔗 Part of the "Ultimate Utility Toolkit"
This tool is part of the **[Anunzio International Utility Toolkit](https://github.com/anzulaqeel/ultimate-utility-toolkit)**.
Check out the full collection of **180+ developer tools, scripts, and templates** in the master repository.

Developed for Anunzio International by Anzul Aqeel.
