# Deploying Flask (WSGI) Applications

These are the files that were used as part of the demo at a presenation for the Flask-NYC meetup group given on June 25th, 2014 at InterviewJet. The slides are located at [Speaker Deck](https://speakerdeck.com/mattupstate/deploying-flask-wsgi-applications)

The `hello_world` folder contains the basic app files.

* app.py - The "hello world" application
* ge.py - The example gevent container
* requirements.txt - The "hello world" app dependencies
* settings.py - The default app settings
* tor.py - The example Tornado container

The `ansible` folder contains the files used by the `deploy.yaml` playbook.

* nginx.conf - The Nginx config template
* settings.py - The "hello world" app override settings
* upstart.conf - The upstate config template

If you want to run the playbook, be sure to install [Ansible](http://www.ansible.com) and [Vagrant](http://www.vagrantup.com).

From the root directory, then run:

    $ vagrant up
