|pypi| |travis| |codecov| |downloads|


edc-label
---------

Print labels from for clinic/edc projects



CUPS and printer Installation
+++++++++++++++++++++++++++++


Install CUPS Print Server::

	sudo apt-get install cups

	sudo cp /etc/cups/cupsd.conf /etc/cups/cupsd.conf.original
	
	sudo chmod a-w /etc/cups/cupsd.conf.original

Edit ``/etc/cups/cupsd.conf`` to listen on the public IP::

	sudo  nano /etc/cups/cupsd.conf

Add the last line with your public IP::

	    Listen 127.0.0.1:631           # existing loopback Listen
	    Listen /var/run/cups/cups.sock # existing socket Listen
	--> Listen PUBLIC_IP:631      # Listen on the LAN interface, Port 631 (IPP)

Restart CUPS::

	sudo systemctl restart cups.service

Add a remote printer to a remote CUPS server
++++++++++++++++++++++++++++++++++++++++++++

``LOCAL_PRINTER_NAME``: printer as named on the EDC, your server

``REMOTE_IP_ADDRESS``: IP of remote CUPS server

``PRINTER_NAME``: printer name installed on remote CUPS server

For example::

	lpadmin -p LOCAL_PRINTER_NAME -E -v ipp://REMOTE_IP_ADDRESS/printers/PRINTER_NAME


Add an IP addressable remote printer 
++++++++++++++++++++++++++++++++++++

``PRINTER_NAME``: printer as named on the EDC, your server

``REMOTE_IP_ADDRESS``: IP of remote printer

For example::

	lpadmin -p PRINTER_NAME -E -v ipp://REMOTE_IP_ADDRESS/ipp/print -m everywhere



See also http://labelary.com/viewer.html


.. |pypi| image:: https://img.shields.io/pypi/v/edc-label.svg
    :target: https://pypi.python.org/pypi/edc-label
    
.. |travis| image:: https://travis-ci.com/clinicedc/edc-label.svg?branch=develop
    :target: https://travis-ci.com/clinicedc/edc-label
    
.. |codecov| image:: https://codecov.io/gh/clinicedc/edc-label/branch/develop/graph/badge.svg
  :target: https://codecov.io/gh/clinicedc/edc-label

.. |downloads| image:: https://pepy.tech/badge/edc-label
   :target: https://pepy.tech/project/edc-label
