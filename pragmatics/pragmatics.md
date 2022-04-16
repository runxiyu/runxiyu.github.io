%%%
title = "Pragmatic Use of Nonfree Software 7"
abbrev = "Pragmatic Use of Nonfree Software"
area = "Free Software"
workgroup = "Free Software Community"
submissiontype = "independent"
ipr = "none"
keyword = ["Nonfree", "Pragmatics"]
#updates = [ 2555, 5540 ]
#date = 2003-04-01T00:00:00Z

[seriesInfo]
name = "Internet-Draft"
value = "Request for Discussions 1"
stream = "independent"
status = "informational"

[[author]]
initials = "A."
surname = "Yu"
fullname = "Andrew Yu"
#role = "author"
organization = "The 2nd School Aff. to FDU"
  [author.address]
  email = "andrew@andrewyu.org"
  uri = "https://www.andrewyu.org/"
%%%

.# Abstract

Free Software is undoubtably a good thing for society.  However, modern computer users are stuck in the proprietary "ecosystem" for historical reasons.  This document describes the author's viewpoint of using proprietary platforms to spread the ideas of Free Software.

.# Status of This Memo

This document is currently in the DRAFT status.

This document describes the author's viewpoint.  This does not represent the ideas of the Free Software Foundation or any other entity.  Distribution of this memo is unlimited.

{mainmatter}

# Introduction

Readers of this memo probably understand the ideals of the Free Software Movement, and avoid proprietary software when possible.  However, as most outsiders are unaware and are deeply buried inside the proprietary dystopia created by mostly multibillion-dollar technology coorporations, our methods of communicating with the masses are ineffective.

In February 2022, the author decided to adjust his dogma, and permitted limited usage of nonfree chat platforms to hopefully spread our ideas to the general public.  This was attempted by registering a Discord account, creating a Guild called "Free Software Introductions", and setting up a basic Discord-to-IRC relay to #fsi on both irc.andrewyu.org and irc.libera.chat.

One of the communities that he knows about, the VF-Technic Minetest community, primarily uses Discord as a means of communication by plays not in-game.  As the users inside are Minetest players, a Free Software voxel sandbox game, similar to but much more flexible and freedom-respecting than Minecraft, it is believed that the users have some contact with Free Software, although they might not understand the freedom part of the issue, i.e. they might be thinking in terms of "open source" instead.  After sharing the invite link in the VF-Technic Guild, some people joined, and we've partially converted two users.

# Justification

Two users is definitely few, but it sets a start and an example for how freedom can be spread.

There are numerous free replacements to proprietary services such as Discord, such as Internet Relay Chat, the Extensible Messaging and Presense Protocol, the Matrix protocol, and email.  As Free Software activists, we generally prefer these protocols over nonfree services.  This section explains the reasons to consider nonfree services and protocols.

Generally, users on IRC and XMPP have a fair understanding of the Free Software Movement, and it is quick and easy to inform them what we mean by "free", "the four freedoms", and similar ideas.  For users on the Libera Chat IRC network, which by far has the most users of any network, it is exceptionally easy to introduce a user into the #fsf channel for discussions with people supporting Free Software.  Introducing ignorant users on these protocols and platforms are a day-to-day simple task.

Furthermore, the amount of users we can reach on these protocols are rather limiting.  Libera has around forty thousand users according to the `USERS` command, and considering the fact that around 90% of these people aren't ignorant, there isn't much we can do.

Matrix users, in particular users of the matrix.org homeserver, typically know but don't completely understand Free Software.  Rather than using Matrix IDs to identify users, the Matrix specification specifies that third-party platform identities, such as email and GitHub, are how users should be referenced both internally by servers and shown to other users.  This is obviously an increadibly foolish idea, especially considering the use of centralized identity servers (similar to X509 certificate authorities) for 3PIDs.  These are our first targets, but these should also be easy to get the idea across.

It is true that Libera Chat and similar IRC networks, though multi-centered in a technical way (i.e. multiple IRC servers form an IRC network), the network is politically centralized, controlled by one entity, Libera.  The Internet Relay Chat server-to-server protocol implies that servers fully trust each other and are expected to not send damaging commands, which in turn implies full trust between server operators, no federation, and political centralization.  The privacy policy and network policy of Libera Chat are in the author's opinion non-intrusive, therefore the use of which is acceptable and is promoted by the FSF.  (Obviously, most methods of using IRC do not involve nonfree software.)

Nevertheless, those that have never touched Free Software are often on giant proprietary platforms, and take these as universal methods of communication.  Many people go months before checking their mailbox (physical or electronic), refuse to use XMPP or IRC for its age.

An alternative protocol, Internet Delay Chat, is being developed.

There is one special case where using some nonfree software, and even urging others to use it, can be a positive thing. That's when the use of the nonfree software aims directly at putting an end to the use of that very same nonfree software.[@!RMSGP]  The author believes that the following fall within this scope:

- Developing a free project that requires nonfree environments to bootstrap;
- To spread awareness of software freedom issues to users in nonfree environments.

As almost all types of development can be done on most types of BSD and GNU operating systems, the author hasn't found any software that fit this category.  Extending the interpretation allos for using nonfree software's behavior as a reference in Free Software development, though an arguable programming practice, may help the community to progress by understanding common features that users of nonfree services use.

The latter is more interesting, as explained above our methods of spreading awareness is limited.

# Action Procedure

Activists **MUST NOT** list such nonfree services in "Contact Information" pages on their website or similar sources, unless followed by a explanation that the purpose of the nonfree platform is to introduce users thereof onto free protocols and to eventually exterminate the nonfree platform.  Whenever these references to nonfree platforms appear, the author **MUST** present free methods of communication.  Activists **SHOULD** pragmatically use as many of the popular free protocols as possible, to ensure that oppurtunities of introductions are not lost.  In cases involving competition between free and nonfree protocols and platforms, ethical concerns (i.e. enabling talking to a new user on any ethical platform) **MUST** take precedence over technical concerns (such as disliking the XMPP protocol for its inefficent use of XML) whenever possible.

Communities for introducing users to Free Software on nonfree platforms **MUST** be bridged to a free protocol in some obvious way, in order to minimize the usage of nonfree platforms even for the purpose of communicating ideology to new users and allow members of the Free Software community refusing to use nonfree platforms in any way to participate.  Usages of nonfree platforms, besides part of the user-introduction process that must happen on the nonfree platform, **SHOULD** be avoided.

For example, the author created a Discord Guild called Free Software Introductions, which is one-way-puppeted to #fsi on irc.andrewyu.org, which is then one-way-puppeted to Libera.  The relay system is sort-of messed up, but it's working.  Inviting new users to it via https://discord.gg/7CYp7ntww7 is good, but as the author has made his own sacrifice already, there exists no need for other existing Free Software activists to join and use it instead of IRC.

# Technical Limitations
The old and centralized nature of IRC, the insane 3PID recommendation of Matrix, the bad routing and efficency of XMPP, and the lack of documentation on PSYC, has led us to develop a new protocol, Internet Delay Chat[@!IDC], which aims to be free, modern (i.e. support for channel groups and shared permission sets, non-text data with MIME types), sane (i.e. TCP, UDP and SCTP-based, instead of HTTP POST APIs) and simple.


# Conclusion

# FSF Considerations

{backmatter}

{numbered="false"}
# Acknowledgements


{numbered="false"}
# Contributors


<reference anchor="RFC2813" target="https://www.rfc-editor.org/rfc/rfc2813.txt">
   <front>
      <title>Internet Relay Chat: Server Protocol</title>
      <author>
         <organization>Internet Engineering Task Force</organization>
      </author>
      <date year="2013" month="September"></date>
   </front>
</reference>
<reference anchor="RMSGP" target="http://www.gnu.org/philosophy/is-ever-good-use-nonfree-program.en.html">
   <front>
      <title>Is It Ever a Good Thing to Use a Nonfree Program?</title>
        <author initials='R.' surname='Stallman' fullname='Richard Stallman'>
            <organization>The GNU Project</organization>
            <address>
                <email>rms@gnu.org</email>
                <uri>https://stallman.org/</uri>
            </address>
        </author>
      <date year="2013" month="September"></date>
   </front>
</reference>
<reference anchor='IDC' target='https://git.andrewyu.org/internet-delay-chat'>
    <front>
        <title>Internet Delay Chat</title>
        <author initials='A.' surname='Yu' fullname='Andrew Yu'>
            <organization>The Second School Affiliated to Fudan University</organization>
            <address>
                <email>andrew@andrewyu.org</email>
                <uri>https://www.andrewyu.org/</uri>
            </address>
        </author>
        <date year='2022' month="April" />
    </front>
</reference>
