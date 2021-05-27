#!/usr/bin/env python2.7
from rrv_vote import getApprovedProjects

budget = 40.0  # million
costs = {
  'lobbying': 3.5,
  'wallet': 21.0,
  'UOI': 40.0,
  #'UOI_1': 10.0,
  #'UOI_2': 10.0,
  #'UOI_3': 10.0,
  #'UOI_4': 10.0,
}
votes = []

# Votes will go here...

# Arc
votes.append({
  'lobbying': {
    # I don't expect any tangible short-term benefit. It may help to raise
    # awareness among politicians and regulatory bodies that there are some
    # political and regulatory road blocks in the way of innovation, but I don't
    # expect it to affect anything short-term. Whatever materials are produced
    # by the effort would likely be at least somewhat specific to some target
    # jurisdiction(s) (e.g. the US).
    'short': .1,
    # Any long-term benefits would have limited jurisdiction, so this doesn't
    # really have the same scale as some of the more technically innovative
    # proposals we've seen. The calculus on this would shift along with the
    # political landscape and changing regulations, so this could change if
    # reviewed again at a later date or as part of a carefully targeted
    # proposal. Right now, I expect technical problems and solutions, not
    # political ones, to make or break things for the PKT community.
    'long': .1,
    # Honestly, I have no idea how to score this one on principle. On the one
    # hand, I tend to think that directly funding political activity should be
    # considered out-of-scope for the NS. On the other hand, in some
    # hypothetical scenario where PKT was effectively banned, then there would
    # be hard to justify funding anything except lobbying. In any case, for this
    # proposal in particular, I don't think the milestone objectives are
    # sufficiently well defined.
    'scope': 0.,
    # The proposal states that each milestone requires the requested PKT or
    # enough to meet some budget requirement in national currency (at whatever
    # the exchange rate is at the time). I don't think that's something the NS
    # can or should agree to. I have to assume that, if the exchange rate
    # dropped and those funds were not made available, then the project wouldn't
    # be completed. That seems like a pointless and unnecessary risk to take,
    # given the volatility of crypto in general right now.
    'risk': 0.,
    # There's some past association between applicants and NS members, which
    # would normally earn a penalty of some kind (perhaps 0.75 or so). However,
    # there's quite a few problems with the application itself, unrelated to the
    # risk and scope of the project:
    #   1. The application is plain text, rather than following the markdown
    #      template. This makes it more difficult to review (both by the NS and
    #      any stake holders who want to monitor what the NS is approving). It
    #      gives the impression of something that was thrown together at the
    #      last minute, in a rush to submit something before the deadline.
    #   2. The application lists a minimum budget in national currency, and
    #      requests that additional funding be made available if the exchange
    #      rate drops. As I noted in the risk criterion, that's not something I
    #      think the NS can or should agree to. If we approve the proposal in
    #      its current state, then it would imply that the NS agrees to make the
    #      additional funds available, even if the exchange rate does not drop.
    #      That would set a precedent that we accept applications with these
    #      kinds of conditions, which I think would go against the interest of
    #      the NS. Note that I think this would be disqualifying by itself, but
    #      if it was the only issue with an otherwise promising application,
    #      then I could possibly be convinced to allow that clause to be
    #      removed.
    #   3. I realize there was some followup on git after the submission window
    #      closed, but we need to judge applications based on their state at the
    #      close of submission, barring exceptional circumstances. Based on that
    #      information, if we convert the budget to an hourly rate, then the
    #      requested amount seems unreasonably high. This is extra problematic
    #      when the applicants include known associates of the NS. Given the
    #      minimum funding requirements (in national currency) mentioned before,
    #      there's some implication that somebody worked out the minimum budget
    #      needed for the proposal to succeed. I think some sort of breakdown of
    #      that information would need to be included in the application,
    #      otherwise we can't really justify the pay relative to hours worked.
    # Taken together, I don't think the NS should accept this application in its
    # current state, even if the project was otherwise in line with the
    # interests of the NS.
    'hazard': 0.,
  },

  'wallet': {
    # As far as I know, this would be the first web-based frontend to a PKT
    # wallet. That at least has some short-term novelty to it.
    'short': 0.5,
    # There amount of long-term utility is more than none, I guess, but I
    # definitely see this as having more short term benefit. Worst case
    # scenario, the code could either be used as a starting point for a new
    # implementation, or an example of what not to do (if it fails for
    # interesting reasons).
    'long': 0.1,
    # It's not clear to me if the intent was to write a new wallet, or use an
    # existing wallet (which?) on the backend. I'll assume the intent is to use
    # whatever the "best" existing wallet is, since this seems to be more about
    # the frontend. Either way, this is yet-another-wallet. I don't think it
    # makes much sense to keep funding wallet projects, since at some point
    # they'll just be fighting over the same body of users. This rating could
    # change if the proposal was resubmitted in the future, depending on how the
    # other wallet projects turn out.
    'scope': 0.,
    # Assuming this is just a front-end, I don't think this is particularly
    # risky as wallet-related projects go. If there weren't already other
    # wallets in the works, then a web-based frontend would probably be one of
    # the less risky projects to fund, in my opinion. That's not the world we
    # live in, so I'm not sure the web based wallet would really attract that
    # many new users (be that from other wallets to itself, or to the PKT
    # community as a whole). On the whole, I see this proposal as kind of risky,
    # since it partly works against the other wallet proposals, but not so bad
    # that it would be disqualifying on its own.
    'risk': 0.5,
    # I don't think the NS should fund a web-based miner. I've come across too
    # many instances of malicious mining code being injected into web pages. If
    # the NS funded development of a web-based miner, and then it found its way
    # into e.g. a malicious advertisement, the negative press from that could be
    # bad for PKT (or at the very least, reflect poorly on the NS). Without that
    # aspect, I think this would be fine from a hazard aspect (but not great
    # overall, due to the relative saturation of wallet projects).
    'hazard': 0.,
  },


  # Note that, upon further reflection, I don't think the NS can accept the
  # applicants' suggestion to split this proposal into 4x 10M proposals and rank
  # them. Or split them at all, for that matter. I don't see a way to split
  # proposals (or otherwise support a flexible budget) within the constrains of
  # the current voting system, and it would be inappropriate to change the
  # voting system after a request for proposals has been issued (not to mention
  # after the deadline passes). I recommend that the NS treats this as a single
  # proposal for the full 40M in the request, on the grounds that this seems to
  # be the least favorable for the applicant (it maximizes the chances that we
  # don't have room for the project in our budget). If the rest of the NS
  # disagrees with my assessment, and wants to keep the 4x 10M proposals, then
  # my vote for those proposals can be assumed to be 0 on the grounds that this
  # is hazardous to the NS.
  'UOI': {
      # It's honestly really hard to judge short short term impact, since the
      # task is inherently open-ended and depends on what projects the UOI
      # decides to fund. For lack of better ideas, I'm assuming the average
      # project the UOI funds would be an average project, so that kind of sets
      # a baseline of 0.5 to go off of for both of these. The UOI can
      # (hopefully) do a better job attracting proposals and vetting/reviewing
      # them, so that adds favorably to the project. At the same time, the
      # projects the UOI chooses to support may not align entirely with the
      # interests of PKT or the NS, so that takes something away. For lack of
      # better ideas, I'm just going to say those two effects probably cancel,
      # so over all I would expect the results of funding the UOI to be about
      # the same as funding an assortment of average projects.
      'short': .5,
      # See above, exact same argument but for long term.
      'long': .5,
      # Bylaw 6, the worst case scenario is that 2/3 of the budget finds its way
      # to projects. If we assume that this is what happens, that the remaining
      # 1/3 is entirely out-of-scope, and that all funded projects are in-scope,
      # then I guess 2/3 is the obvious thing to put here. In reality, I guess
      # the funds spent on something other than regular projects should be less
      # than 1/3, and some fraction of that would be on things that are at least
      # tangentially aiming in the right direction (e.g. support projects), so
      # hopefully I'm being unnecessarily harsh here.
      'scope': 2./3.,
      # The risk here comes from basically two parts.
      #   1: 0.8 based on the risk that the UOI fund does not spend the funds on
      #      appropriate projects. This could happen if there are no
      #      (reasonable) applications to the UOI fund, or if the fund chooses
      #      to accept projects that aren't well aligned with the scope / the
      #      interests of the NS.
      #   2: 0.8 based on the average risk of the individual projects accepted
      #      by the UOI fund. I haven't gone through the history to check, but I
      #      think this is probably better than the risk I would assign an
      #      "average" proposal to the NS. I'm operating under the assumption
      #      that the UOI fund would receive applications of a similar quality,
      #      but the fund has the resources available to better review and vet
      #      the proposals and their applicants, so they should tend to reject
      #      the bad ones. This (hopefully) biases the risk criterion towards
      #      better projects, and it's the main thing that (arguably) justifies
      #      the overhead accounted for in the scope criterion (other than being
      #      less work for the NS and more convenient for applicants who prefer
      #      to be funded in euros rather than PKT).
      # These numbers are admittedly a little arbitrary. Theoretically, I guess
      # I should look through past applications, figure out the distribution of
      # submitted to accepted applications, and the success ratio of accepted
      # ones, and use that to calibrate my projection of the average risk of
      # projects. I don't think our sample size is large enough to be
      # statistically significant, and the UOI fund may attract a more diverse
      # pool of applicants (I would hazard to guess that more people are
      # comfortable doing work payed in euros than in cyrptocurrency).
      'risk': 0.64,
      # CJD is involved, which could look like favoritism. For any meta-project
      # of this style to succeed, at least starting out, it's probably going to
      # need some amount of feedback from the NS. So I think it's good that CJD
      # is involved, but it still looks bad compared to a project with no
      # involvement by NS members (and no conflicts of interest or other hazards
      # to get in the way).
      'hazard': 0.5,
  }
})

# Caleb
votes.append({
  'lobbying': {
    # This proposal is about building a non-partison lobbying campaign for Internet freedom, decentralization and
    # privacy. It has been said that if you don't tell your story then someone else will, and we have already begun
    # to see blockchain, crypto mining, privacy, and end-to-end encryption being cast in negative light. The US and EU
    # governments have been mulling bans on end-to-end encryption or mandatory backdoors, and cryptocurrencies are
    # increasingly are coming under regulatory scruteny with some discussion of outright bans on privacy coins such as
    # Monero. There is also an apparent PR war against crypto mining, with its supposed environmental impact getting
    # more media attention than that of even oil and coal exploration.
    #
    # The communities around these technologies have clearly been bad at explaining their importance to society, and I
    # think there is very real possibility that governments around the world will begin to turn their backs on freedom
    # of communication, which would have very real short term impact on the ability of PKT to fulfill the vision.
    'short': 3/5.0,

    # It has been said that the price of liberty is eternal vigilance, and to this day we see autocracy,
    # totalitarianism, and oppression being proposed as "for the greater good", despite their historically poor
    # longevity and association to some of the most horrible atrocities in history.

    # Blockchains enable individuals to leverage simple freedom of communication and organize themselves in ways
    # that were previously not possible without dependence on government, existing businesses, and the banking
    # system. This puts blockchain at the forefront of the struggle for individual liberty, but blockchain
    # communities currently do not make significant concerted efforts to promote the freedoms upon which they
    # depend. So I think there is a long term necessity to continue to communicate about the importance of end-to-end
    # encryption, open source software, freedom of communication, privacy, and decentralization.
    'long': 4/5.0,

    # The project proposal does not follow the standard template which makes it difficult to understand, but it does
    # seem to have strong success criteria for the amount of declared work. The declared work seems to be 320+80+160+160
    # hours (or roughly 4.8 person-months) and the cost seems to be 3.5 million PKT. As the current price in the informal
    # trading chat seems to be roughly 5 cents, this makes the average hourly cost about 243 dollars per hour which is
    # a bit high. Furthermore there is a disclamer where it is mentioned that the milestones require 75k, 50k, and 50k
    # USD respectively which comes to the same numbers. Unfortunately the project is proposed in such a way that in case
    # of a rise in PKT price, the applicant wishes still to receive the entire payment but in case of a drop in PKT price,
    # they wish the payment to be more. I'm not ready to fail the project on this point but I think it has serious flaws.
    'scope': 1/5.0,
    
    # It is difficult to understand what is being requested, but the project proposal seems not to ask for any payment
    # until after the first deliverables are provided. The payment seems to be well spaced across the milestones, but
    # there seem to be many "extra options" and it is unclear if the applicant expects the Network Steward to vote on
    # each one of these as though it were a separate project, or which of these may or may not be included in the
    # declared time effort. My feeling is that if the proposal were re-phrased to be clear, then it would have fairly
    # good risk control, but as of now, the biggest risk is that the Network Steward might mis-interpret the proposal
    # and disagree with the applicant as to which milestones were delivered and what should be paid out, or how much
    # PKT should be paid, as the applicant is unsure if 3.5mn PKT is enough. I think I have to fail this project for
    # being under-specified, it is a good overall idea but the application is not developed enough to be handled
    # directly by the Network Steward.
    'risk': 0/5.0,

    # As far as conflicts, the template was not used and the declaration is missing. There is a "minor" relationship
    # between Anode LLC (myself / Adonis) and one of the project participants (Alex Lightman), as he is also in a
    # software development contract with Anode. I don't think the applicant was intentionally hiding this fact, nor
    # that this constitutes a conflict for which we should step out from evaluation.
    # As far as "unfairly benefitting any one participant over any other", the hourly costs in the project are high
    # and it is unclear whether the declared hours are for the plain project or the project with "add-ons" included.
    # Most problematically, the costs are expressed in a "rachet" form where the applicant expects costs covered in
    # case of a decrease in PKT price but wants to keep the difference in case the price should go the other way.
    'hazard': 2/5.0
  },

  'wallet': {
    # Despite significant Network Steward support in the past, the wallet story is clearly not the strongest aspect of the PKT project.
    # There are currently 3 different wallets, a command line wallet which is robust but not user friendly, an electrum based
    # wallet which is user friendly but not robust enough to support thousands of payments which occur when mining, and Zulu
    # which is a GUI frontend for the command line wallet, but which only works on Apple computers.
    # There is an entirely separate wallet in development by the team who produces OpenTransactions, but this has not yet been released.

    # My observation is that there is an abundance of wallet "technology" but a lack of "product", so for example technical
    # support ends up falling on the open source community which means it inevitably has a "helping eachother" aesthetic
    # rather than one of a smooth experience with a complete product.

    # It is my opinion that the PKT community needs a business to step up and build a wallet product which has a financial model
    # that puts the customer in charge. The development of additional open source wallet technologies by the Network Steward is
    # certainly not worthless, but in my evaluation it does not meet the current pressing need.
    'short': 3/5.0,

    # This project is not described in terms of long term impact to decentralizing internet infrastructure. One might argue that
    # short term impact drives long term impact, but short term impact has it's own category in this evaluation.
    'long': 0/5.0,

    # Any endevor to build a crypto wallet must necessarily be based on either existing wallet technology such as PKTWallet
    # or ElectrumX, or on an entirely new wallet technology. Ideally a proposal such as this would specify whether it is to be
    # based on new or existing technology, and in the case of new tech to explain why it is important to have this new technology
    # and how it would work, and in the case of existing technology, to give a brief rundown of the tech stack so that
    # feasibility, cost, and risk can be evaluated. Since this proposal did not provide any of these details, we need to make a
    # guess as to intent, with an eye to the minimum deliverable that would satisfy the success criteria.
    # Since the proposal says "everybody should be able to send and recieve PKT" it seems that the focus is more about bringing
    # technology to the consumer rather than creating new technology, so I think it is fair to assume that the intent is to
    # leverage existing technology, which is also the cheaper option.
    # Building a new wallet based on existing technology should probably take somewhere around 1 person-month of effort to specify
    # and design, 3 PMs to develop and test and 1 PM to manage, which comes out to 5 PMs total. So the proposal's estimate of 10 PMs
    # is perhaps high, but not ridiculous.
    # On cost, the current price of PKT in informal trading seems to be roughly 5 cents, this places the total project cost at
    # 1,050,000 and thus the person-month cost at 105,000.
    # Assuming every month to be 4 40 hour weeks of fulltime work, the cost would be around 650$/hr which is very high.
    # I'm not going to outright fail the project on this point but I would only be inclined to accept a project of this cost if
    # there was nothing better.
    'scope': 1/5.0,

    # There are 5 milestones and payouts are reasonably spaced. Without knowing what existing wallet technology this project would
    # be based on, or if new, how the new wallet technology would work, I can't reasonably give this better than 2 of 5.
    'risk': 2/5.0,

    # On the question of hazard, the checkboxes for declaration of conflicts were not filled, but I don't know the applicant
    # and don't know of any conflicts myself. However the applicant is asking for what is, if we consider the informal trading
    # chat quote of 5 cents, over a million dollar grant. I see no mention of any business entity which would be in charge of the
    # project so it appears as though an individual would be receiving the funds. It is very irregular for an individual to receive 
    # a grant of over 1 million dollars in value rather than an entity with a public accountant. Also if the price of PKT were to
    # rise in the next couple of months, there is no provision in this project for the applicant to receive partial payout for
    # subsequent milestones which means this project could conceivably become worth tens of millions of dollars and have an
    # effective person-month rate of tens of thousands of dollars per hour so in my opinion this project fails the test of
    # "without unfairly benefitting any one participant over any other" and I am going to fail it on hazard control.
    'hazard': 0/5.0,
  },

  # Because there is a conflict, I have mechanically set the UOI rating to the average of the others, however
  # I have set hazard to zero instead of one because I have failed both of the other projects so is it best
  # in keeping with the intent of non-intervension for reason of conflict that I also fail the UOI project.
  'UOI': {
      'short': 3/5.0,
      'long': 2/5.0,
      'scope': 1/5.0,
      'risk': 1/5.0,
      'hazard': 0/5.0,
  },
})

print "WINNING PROJECTS: %s" % getApprovedProjects(budget, costs, votes)

projects = {}
for x in votes[0]:
    projects[x] = { 'short': 0., 'long': 0., 'scope': 0., 'risk': 0., 'hazard': 0. }
for r in votes:
    for x in r:
        ## x = repo, price_display, etc
        for y in projects[x]:
          projects[x][y] += r[x][y]
trans = {
    'short':  "Short term impact         ",
    'long':   "Long term impact          ",
    'scope':  "Scope and use of resources",
    'risk':   "Risk control              ",
    'hazard': "Hazard control            "
}
for p in projects:
    print p
    for q in projects[p]:
        print "  ", trans[q], projects[p][q]
