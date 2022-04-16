%%%
title = "Pragmatic Use of Nonfree Software"
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
initials = "A. Yu"
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

This document describes the author's viewpoint.  This does not represent the ideas of the Free Software Foundation or any other entity.  Distribution of this memo is unlimited.

{mainmatter}

# Introduction

Readers of this memo probably understand the ideals of the Free Software Movement, and avoid proprietary software when possible.  However, as most outsiders are unaware and are deeply buried inside the proprietary dystopia created by mostly multibillion-dollar technology coorporations, our methods of communicating with the masses are ineffective.

In February 2022, the author decided to adjust his dogma, and permitted limited usage of nonfree chat platforms to hopefully spread our ideas to the general public.  This was attempted by registering a Discord account, creating a Guild called "Free Software Introductions", and setting up a basic Discord-to-IRC relay to #fsi on both irc.andrewyu.org and irc.libera.chat.

One of the communities that he knows about, the VF-Technic Minetest community, primarily uses Discord as a means of communication by plays not in-game.  As the users inside are Minetest players, a Free Software voxel sandbox game, similar to but much more flexible and freedom-respecting than Minecraft, it is believed that the users have some contact with Free Software, although they might not understand the freedom part of the issue, i.e. they might be thinking in terms of "open source" instead.  After sharing the invite link in the VF-Technic Guild, some people joined, and we've partially converted two users.

Two users is definitely few, but it sets a start and an example for how freedom can be spread.

There are numerous free replacements to proprietary services such as Discord, such as Internet Relay Chat, the Extensible Messaging and Presense Protocol, the Matrix protocol, and email.  As Free Software activists, we generally prefer these protocols over nonfree services.  This section explains the reasons to consider nonfree services and protocols.

Generally, users on IRC and XMPP have a fair understanding of the Free Software Movement, and it is quick and easy to inform them what we mean by "free", "the four freedoms", and similar ideas.  For users on the Libera Chat IRC network, which by far has the most users of any network, it is exceptionally easy to introduce a user into the #fsf channel for discussions with people supporting Free Software.  Introducing ignorant users on these protocols and platforms are a day-to-day simple task.

Furthermore, the amount of users we can reach on these protocols are rather limiting.  Libera has around forty thousand users according to the `USERS` command, and considering the fact that around 90% of these people aren't ignorant, there isn't much we can do.

Matrix users, in particular users of the matrix.org homeserver, typically know but don't completely understand Free Software.  Rather than using Matrix IDs to identify users, the Matrix specification specifies that third-party platform identities, such as email and GitHub, are how users should be referenced both internally by servers and shown to other users.  This is obviously an increadibly foolish isea, especially considering the use of centralized identity servers (similar to X509 certificate authorities) for 3PIDs.  These are our first targets, but these should also be easy to get the idea across.

# The Plan

But there is one special case where using some nonfree software, and even urging others to use it, can be a positive thing. That's when the use of the nonfree software aims directly at putting an end to the use of that very same nonfree software.[@!RMSGP]

# Technical Limitations

git://git.andrewyu.org/internet-delay-chat

# Conclusion

Hi

# FSF Considerations

Hi

{backmatter}

{numbered="false"}
# Acknowledgements

Many thanks to iShareFreedom, qrpnxz, DiffieHellman, Leah Rowe and many others for the ideas (and rebutted arguments) in this article.

{numbered="false"}
# Contributors

Many thanks to everyone in the Free Software community for the freedom we have today.

<reference anchor="RMSGP" target="http://www.gnu.org/philosophy/is-ever-good-use-nonfree-program.en.html">
   <front>
      <title>Is It Ever a Good Thing to Use a Nonfree Program?</title>
      <author>
         <organization>The GNU Project</organization>
      </author>
      <date year="2013" month="September"></date>
   </front>
</reference>

