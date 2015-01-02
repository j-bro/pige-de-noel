#Pige de Noël
###A webapp to assist your Secret Santa planning

The app will support creating groups of participants and gift exchanges between them.
An administrator creates a group and adds participants.
When an exchange is activated, participants will be assigned a secret santa at random from the group.
Participants can provide a gift list that will be viewable by their secret santa.

Currently a work in progress, not at all functional for the moment.

## Groups
**Status: incomplete**
Groups contain a minimum of 3 participants.
Participants can be added by the administrator when the group is created or later on from the group management page.
Participants will receive a link to join the group. The link is not specific to their email address and could potentially be used by someone else if it were to be forwarded (however each link can only be used once).

## Exchanges
**Status: incomplete**
An exchange can be created within a group of participants.
Multiple exchanges per group are supported.
Each exchange has its name and optional price limit.


## Authentication
**Status: incomplete**
Authentication is handled through Google Accounts using the Google App Engine users API.

When the administrator creates the group, participants will receive an invitation to join the group by email.
By clicking on that link, they will be taken to the login page, where they must login with a Google account*. After logging in, the invitation to join the group will be accepted and they will be taken to their participation page. 

*While participants must login using a Google Account, they are free to change their email address for communication later through the user settings page at the the top-right of the nav bar.