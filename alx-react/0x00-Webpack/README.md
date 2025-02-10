## RBasic Webpack Setup

### Introduction

This project demonstrates a basic setup for using Webpack, a powerful tool for bundling JavaScript modules. The goal is to create a simple environment where you can install and run Webpack using npm.

### Prerequisites

- **Node.js and npm**: Ensure you have Node.js and npm installed on your system. You can verify this by running `node -v` and `npm -v` in your terminal.

### Basic Setup

#### Step 1: Create a Project Folder

Create a new folder named `task_0` to serve as your project directory.

```bash
mkdir task_0
cd task_0
```

#### Step 2: Initialize npm

Initialize a new npm project by running the following command. This will create a `package.json` file with default settings.

```bash
npm init -y
```

#### Step 3: Install Webpack and Webpack CLI

Install Webpack and Webpack CLI as development dependencies using npm. This is recommended over a global installation to manage versions per project.

```bash
npm install --save-dev webpack webpack-cli
```

### Running Webpack

After installation, you can run Webpack using the command line interface (CLI) provided by `webpack-cli`. To do this, you can either use `npx webpack` or add a script to your `package.json` file.

#### Option 1: Using npx

You can run Webpack directly using `npx` without adding it as a script:

```bash
npx webpack
```

#### Option 2: Adding a Script to package.json

Alternatively, you can add a script to your `package.json` file to run Webpack more conveniently:

```json
"scripts": {
  "build": "webpack"
}
```

Then, you can run Webpack by executing:

```bash
npm run build
```

### Next Steps

- **Create Entry and Output Files**: Set up an entry point (e.g., `index.js`) and an output directory (e.g., `dist`) to bundle your JavaScript files.
- **Configure Webpack**: Create a `webpack.config.js` file to customize the bundling process, such as specifying entry points and output files.

### Conclusion

This basic setup provides a foundation for using Webpack in your projects. You can now expand upon this setup by adding more configurations and plugins to suit your development needs.

---

### Contributing

Contributions are welcome! Feel free to enhance this setup by adding more features or configurations.

### License

[Insert License Information Here]

---

### Acknowledgments

- [Webpack Documentation](https://webpack.js.org/)
- [npm Documentation](https://docs.npmjs.com/)

Citations:
[1] https://ioflood.com/blog/webpack-npm/
[2] https://www.linkedin.com/pulse/getting-started-webpack-step-by-step-guide-beginners-amit-biswas-sgi0c
[3] https://wpshout.com/webpack-tutorial-for-beginners/
[4] https://github.com/gokulkrishh/how-to-setup-webpack-2/blob/master/README.md
[5] https://webpack.js.org/guides/getting-started/
[6] https://pusher.com/tutorials/webpack-part-1/
[7] https://rapidevelop.org/javascript/install-webpack-5
[8] https://github.com/webcrumbs-community/webcrumbs/wiki/Resources:-Setting-up-a-basic-Webpack-project
[9] https://webpack.js.org/guides/installation/