

# Ciena MDSO Collection

The Ansible Ciena MDSO collection includes a variety of Ansible content to help automate the management of Ciena MDSO Orchestration system.

This collection has been tested against MDSO 20.06

## Ansible version compatibility

This collection has been tested against following Ansible versions: **>=2.9.10,<2.11**.

## Included content

<!--start collection content-->

### Supported APIs
| Name                        | Description                  |
| --------------------------- | ---------------------------- |
| [ciena.mdso.domains]        | orchestration domains        |
| [ciena.mdso.domain_types]   | orchestration domain_types   |
| [ciena.mdso.products]       | orchestration products       |
| [ciena.mdso.resources]      | orchestration resources      |
| [ciena.mdso.resource_types] | orchestration resource_types |
| [ciena.mdso.relationships]  | orchestration relationships  |

<!--end collection content-->
## Installing this collection

Install the Ciena MDSO collection with the Ansible Galaxy CLI:

```bash
ansible-galaxy collection install ciena.mdso
```

You can also include it in a `requirements.yml` file and install it with `ansible-galaxy collection install -r requirements.yml`, using the format:

```yaml
---
collections:
  - name: ciena.mdso
```

## Using this collection

### Using modules from the Ciena MDSO collection in your playbooks

You can call modules by their Fully Qualified Collection Namespace (FQCN), such as `ciena.mdso.resources`.

```yaml
---
- hosts:
  - localhost
  vars:
    mdso_creds: &mdso_creds
      mdso_hostname: 10.10.10.10
      mdso_username: admin
      mdso_password: adminpw
  collections:
  - ciena.mdso
  gather_facts: false
  tasks:
  - name: get resources
    resources:
      <<: *mdso_creds
      state: get
```

## Contributing to this collection

We welcome community contributions to this collection. If you find problems, please open an issue or create a PR against the [Ciena MDSO collection repository](https://github.com/ciena/ciena.mdso).

Release is done automatically use Github Actions as part of merging to master.

## Changelogs

[CHANGELOG](CHANGELOG.md)

## Roadmap

* build a roadmap

## More information

- [Ansible network resources](https://docs.ansible.com/ansible/latest/network/getting_started/network_resources.html)
- [Ansible Collection overview](https://github.com/ansible-collections/overview)
- [Ansible User guide](https://docs.ansible.com/ansible/latest/user_guide/index.html)
- [Ansible Developer guide](https://docs.ansible.com/ansible/latest/dev_guide/index.html)
- [Ansible Community code of conduct](https://docs.ansible.com/ansible/latest/community/code_of_conduct.html)

## Licensing

See [LICENSE](LICENSE) to see the full text.

