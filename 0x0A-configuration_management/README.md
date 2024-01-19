# 0x0A. Configuration management

## Configuration Management with Puppet

This repository contains Puppet manifests for tasks related to configuration management. The tasks are designed to familiarize users with basic Puppet syntax and best practices.

## Background

The inspiration for this project comes from a real-world incident experienced by Sylvain Kalache while working on an auto-remediation tool named Skynet at SlideShare. A bug in the code led to unintended consequences, emphasizing the importance of robust configuration management tools like Puppet.

Read more about Sylvain's experience [here](https://twitter.com/devopsreact/status/836971570136375296).

## Resources

Before getting started, it's recommended to go through the following resources:
- [Intro to Configuration Management]((https://www.digitalocean.com/community/tutorials/an-introduction-to-configuration-management)
- [Puppet resource type: file](https://www.puppet.com/docs/puppet/5.5/types/file.html)
- [Puppet’s Declarative Language: Modeling Instead of Scripting](https://www.puppet.com/blog)
- [Puppet lint](http://puppet-lint.com/)
- [Puppet emacs mode](https://github.com/voxpupuli/puppet-mode)

## Requirements

Ensure that your environment meets the following requirements:

- All files are interpreted on Ubuntu 20.04 LTS.
- All files end with a new line.
- A `README.md` file at the root of the folder of the project is mandatory.
- Puppet manifests must pass puppet-lint version 2.1.1 without any errors.
- Puppet manifests must run without error.
- Puppet manifests' first line must be a comment explaining what the Puppet manifest is about.
- Puppet manifest files must end with the extension `.pp`.

**Note on Versioning:** Your Ubuntu 20.04 VM should have Puppet 5.5 preinstalled.

### Installation

#### Puppet

```bash
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet
