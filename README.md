# Goosebot
A tool bot for managing small, personal Discord servers written in Python and hosted using Docker and AWS EC2.

Developed and hosted by Gaelan O'Shea-McKay as a personal project.

### Configuration

##### Environment File
An environment file, `environment.env`, is expected by the bot and must be defined by the developer.

It should contain:\
`BOT_TOKEN=<your_bot_token>`\
`REACTION_ROLE_MESSAGE_ID=<your_message_id>`\
`NOTIF_SUB_MESSAGE_ID=<your_message_id>`\
`SUB_CHANNEL_ID=<your_channel_id>`\
`HOURLY_MESSAGE_CHANNEL_ID=<your_channel_id>`\
`DAILY_MESSAGE_CHANNEL_ID=<your_channel_id>`

This file should *not* be committed to a public repository because it contains the private bot token. Doing so will reset the token and prompt an angry message from Discord.

##### Emoji -> Role Dictionary

The relationship between which emoji are used and which roles are assigned is defined in an external python file containing only an emoji name/emoji ID -> Role ID dict called `external_emoji_dict`. 

Because the emoji and roles that suit each individual Discord community vary, this file is not included in the project and must be defined.

Alternatively, a basic example dict with some simple roles and emoji is commented out in the file and is available for sample use.
### Bot Features

#### Hourly Messages

The bot can send a message to a given channel on the hour, every hour.

The message: `HOURLY_MESSAGE`\
The channel to send it in: `HOURLY_MESSAGE_CHANNEL_ID`

Hourly messages can be toggled on and off with the `.hourly` command.

#### Daily Messages

The bot can send a message to a given channel at a given time every day.

The message: `DAILY_MESSAGE`\
The channel to send it in: `DAILY_MESSAGE_CHANNEL_ID`\
The time of day to send it in (in UTC): `DAILY_MESSAGE_TIME`

Hourly messages can be toggled on and off with the `.daily` command.

#### Reaction Roles

The bot can assign/un-assign roles based on adding/removing reactions to a message.

The idea of the current iteration of the bot is to have one message concerning channel access roles and one message concerning notification subscription roles, but the actual use case of the feature is up to the individual community that uses it.

#### Manual Role Management

Manual role management is available via command line commands.

##### Commands

`.roles` \
Lists the roles that belong to the user and the roles available on the server.

`.role` `<rolename>` `<nickname>`

Assigns the role named `rolename` to the user named `nickname`. If `nickname` is left blank, the role will be self-assigned.

