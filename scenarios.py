"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.

    "appeals" a list of texts to submit and then appeal, with a "reasoning".
              Added for criterion 4; run_eval.py::run_appeals runs it.
"""

SCENARIOS = [
    {
        "name": "my own writing",
        "criterion": 1,
        # ⚠️ PUT YOUR OWN WRITING HERE. Not AI text, not a sample from the web —
        # things you actually wrote. This is the criterion that matters most and
        # it's meaningless with someone else's prose.
        "texts": [
            "Hello Summer,\n Thank you for reaching out to me! Sorry for a late response,it's been a busy week. I'm interested in interviewing for this SDE II position in Amazon. We can connect next week anytime and any day except Tuesday 11 am-12 pm PST. Let me know your availability. Thanks!",
            "I got scared about all this planning. Interestingly I haven't even had said my plan out loud or talked to even my husband. He told me that his manager is unhappy with his work and he has to deliver something substantial this month to handle his annual review which occurs in July. He is really stressed and is now working hard for it. There has been a strange possibility of a new low where we both might get unemployed. We would have to then leave the country. Though there is another aspect where he could deliver and continue with his work but would be always worried and stressed. There could be another possibility that he switches to a different company and things get much more sorted. But yea I guess itna tension kabi nahi hua hoga usko and muje and I'm just looking for ways to get out of this stress, out of this lack of opportunities or money.",
            "So, Repairify is a company where we work with car diagnostics, when a car goes to the garage for getting repairs, there's where Repairify devices kick in. Technicians have these devices, which once they plug in the car, it can give them all the faults solved. So, one of the devices is, let's say, if they have the basic package, that means the devices, once it is plugged in, the car will figure out what's wrong with the car with some DTC codes, which is called diagnostic fault codes. So, generally, we give them back, and then the technicians look into those and see what's wrong with the car and make the changes.But then there are other garages who require a more advanced support from Repairify. So, we have repair technicians at Repairify end who do desk job. Once they get the codes, determine what's wrong with the car and then share the steps to fix those errors and then the technician in the garage just performs them.",
            "I am Monika Daryani, a graduate student in Computer Science at Texas A&amp;M University. I am very\n"
            "interested in interviewing with AMD for internship in &lt;NLP / DL / ML / DS&gt; for Summer 2020.\n"
            "Presently, I am a first year master’s student in Computer Science with 4.0 GPA and a thesis focused\n"
            "on Natural Language Processing. Under the guidance of Dr James Caverlee, my research focuses on\n"
            "using state of the art techniques in NLP and Deep learning to detect fraudulent reviews and postings\n"
            "on e-commerce sites.\n"
            "My most recent project uses BERT and an ensemble of classifiers to solve daily problems like finding\n"
            "news posts with hidden propaganda. Me and my team will be submitting this project to SemEval at\n"
            "ACL Conference 2020.\n"
            "Prior to my masters, I have 4+ years of experience working as a Lead Engineer at Samsung\n"
            "Research. I worked on the Bixby voice assistant team where I built the intent classification system for\n"
            "non-native English speakers for better access to voice assistants in India.\n"
            "I’d love to interview for the &lt;Machine Learning Research Intern&gt; position at &lt;Bloomberg&gt; and based\n"
            "on the position requirements and my qualifications, I will be a great fit for the role.\n"
            "I have attached my resume here for your reference",
            "Magic of past is science of today. Who knew that just saying mantras like “Ok Google” or "
            "“Hey Siri” would play the song you like or call a friend? Isn’t this similar to Aladdin rubbing "
            "a lamp and asking his genie to do something? Having a background in Computer Science, I "
            "found something close to my genie in Natural Language Processing (NLP) and Machine "
            "Learning. My goal is to help machines understand humans in whatever manner or language "
            "they speak and act accordingly. I strongly believe that MS in CS will help me continue this "
            "penchant for bringing magic to life. "
            "Previously, I worked as a Lead Engineer at Samsung Research. Over 4 years that I spent there, I worked across several domains, the latest of which was Bixby Voice assistant, where I worked with Samsung’s voice assistant engineers and scientists. Before that I have worked as a Project lead for several Samsung devices, managing their software development lifecycle from design, all the way through to final software sign off for release to market. "
            "Things you won’t find on my resume are that I’m a very inquisitive person, and am eager to learn new things and apply them to a real world example. "
            "You can see that in my projects as well. Given the scale of Amazon, I believe I would have something new to learn every single day which is why I’m excited for this interview.",
            "Someone once told me if u doubt yourself if you're a good mom or not, you probably are coz bad moms don't really doubt themselves. 🙃\n"
            "\n"
            "Maybe you can try calming yourself also when you are calming the baby. There is this anxiety which triggers in moms when their babies cry, that doesn't happen with dads also. It is sort of maternal instinct and hormonal. So even when the baby is not calming, just tell yourself she is safe and fine and will calm and sleep eventually. Maybe she is trying to get more time with mom 😉.  It's all okay!",
            "Our method also has some limitations. First, the "
            "major drawback occurs because the data is labeled "
            "synthetically. Hence, there is no way to find the "
            "actual recall for our approach. Calculating recall re- "
            "quires manual labeling of all product-review pairs, "
            "which is an expensive process. Second, our method "
            "is dependent on the accuracy of labeling methods. "
            "For the intra-category case, our method cannot de- "
            "tect products hijacked with similar wording in the "
            "same category since their Jaccard distance is low. "
            "For example, if there are two products, “iPhone "
            "X” and “iPhone 5C cover”, the products will have "
            "a low Jaccard distance, and the reviews hijacked "
            "among them cannot be labeled correctly. There- "
            "fore, our ML model can also not learn this kind "
            "of review hijacking. Third, generic reviews like "
            "“Good product!” and “Product shipped fast” were "
            "labeled hijacked and not hijacked depending on "
            "what product they belonged to. Ideally, we would "
            "want to label all of them as not hijacked. This "
            "random labeling adds to the noise in the labels.",
            "We need this bill to claim re-imbursement from my company. I have "
            "bill till 4 Feb. Can u please check once if u can generate a bill "
            "of short cycle. 5-Feb to 10-Feb or so on pro-rata basis ?\n"
            "Next bill cycle starting at 11-Feb. Do check if anything is "
            "feasible. I will need it by next week.\n"
            "Please check if anything is possible. ",
            "I'm gonna write 3 things I'm grateful for. First, I'm grateful for my husband who let's go things that make him mad so easily. Who is silly and funny when required but handles things with so much patience."
            "Second, Grateful for the present, the beautiful house I live in. My beautiful, smart, active daughter. She is the best ever. I love her so much. Third, my friends. Meghana staying here is so good, she helps so much. Other friends whom I can depend on and how everyone fo them is really good!",
            "My name is Monika. I'm 34 years old. My birthday is this month. I have no plans for my birthday, what should I do? Maybe I can setup a home gym for myself for my birthday. I need to order few things for it."
        ],
    },
    # Criterion 2 runs as two scenarios so the report keeps the groups apart:
    # compare the two groups' average combined_score, trial by trial.
    {
        "name": "spread: AI group",
        "criterion": 2,
        # Written by Claude in its ordinary answer voice, one draft each, and
        # put here without scoring them first.
        "texts": [
            "Regular exercise offers a wide range of benefits for both physical "
            "and mental health. It strengthens the heart, improves circulation, "
            "and helps maintain a healthy weight. In addition, physical activity "
            "releases endorphins, which can reduce stress and improve mood. "
            "Experts recommend at least 150 minutes of moderate exercise per "
            "week, such as brisk walking or cycling. Even small changes, like "
            "taking the stairs instead of the elevator, can make a meaningful "
            "difference over time. By making exercise a consistent part of "
            "daily life, individuals can enjoy greater energy, better sleep, and "
            "improved overall well-being.",

            "Learning a new language is a rewarding experience that opens doors "
            "to new cultures and opportunities. It can improve memory, enhance "
            "problem-solving skills, and even delay cognitive decline. To learn "
            "effectively, it is helpful to practice a little every day rather "
            "than studying for long periods once a week. Language learning apps, "
            "conversation partners, and immersive media such as films and "
            "podcasts can all support progress. While the process can feel "
            "challenging at first, consistency and patience are key. Over time, "
            "learners often find that their confidence grows along with their "
            "vocabulary.",

            "Climate change is one of the most pressing challenges facing the "
            "world today. Rising global temperatures are causing more frequent "
            "extreme weather events, melting polar ice, and rising sea levels. "
            "These changes have significant impacts on ecosystems, agriculture, "
            "and human communities. Addressing climate change requires action at "
            "multiple levels, from international agreements to individual "
            "choices. Transitioning to renewable energy, improving energy "
            "efficiency, and protecting forests are all important steps. By "
            "working together, governments, businesses, and individuals can help "
            "build a more sustainable future for generations to come.",

            "Effective leadership is essential for the success of any "
            "organization. A good leader communicates a clear vision, sets "
            "achievable goals, and motivates team members to perform at their "
            "best. Strong leaders also listen actively, provide constructive "
            "feedback, and recognize the contributions of others. In today's "
            "rapidly changing work environment, adaptability has become an "
            "increasingly valuable leadership quality. Leaders who remain open "
            "to new ideas and encourage collaboration are better equipped to "
            "navigate uncertainty. Ultimately, great leadership is about "
            "empowering others and creating an environment where everyone can "
            "thrive.",

            "Reading regularly has many benefits that extend far beyond "
            "entertainment. It expands vocabulary, improves concentration, and "
            "strengthens analytical thinking. Fiction in particular can increase "
            "empathy by allowing readers to experience the world from different "
            "perspectives. Reading before bed can also be a relaxing alternative "
            "to screens, helping to improve sleep quality. To build a reading "
            "habit, it can help to set a small daily goal, such as ten pages, and "
            "to keep a book within easy reach. With time, reading can become an "
            "enjoyable and enriching part of everyday life.",
        ],
    },
    {
        "name": "spread: human group",
        "criterion": 2,
        # Filled in below the list: the first five pieces of "my own writing",
        # chosen by position, not by score.
        "texts": [],
    },
    {
        "name": "label coverage",
        "criterion": 3,
        # Inputs spread across your score range, so you can check all three
        # labels are actually reachable.
        "texts": [
            # Written in the chatbot register on purpose: even sentences,
            # "First/Second/Third", stock transitions. Scored 0.854 (ai).
            "Time management is one of the most important skills a student can develop. "
            "It allows students to balance their academic responsibilities with their personal lives and reduces stress. "
            "There are several strategies that can help students manage their time more effectively. "
            "First, creating a weekly schedule helps students plan their tasks and set clear priorities. "
            "Second, breaking large assignments into smaller steps makes them easier to complete. "
            "Third, limiting distractions such as social media allows students to stay focused on their work. "
            "Additionally, it is important to set aside time for rest, because regular breaks improve concentration and overall productivity. "
            "Ultimately, students who manage their time well are better prepared to achieve their goals and succeed in their future careers.",
            # My own writing, chosen because I know a person wrote it, not for
            # its score. It scored 0.563 (unsure) when I checked.
            "Hug yourself because you're amazing. You are amazing and proud. "
            "Sia will absorb my energy. "
            "I'm building a habit to love myself. Because it feels good and I want to feel good.",
            # Plain workplace update, neither chatbot nor personal. Scored 0.529
            # (unsure): model 0.62 leans AI, style 0.44 leans human, so the
            # split rule also caps it below the AI label.
            "Our team switched to a new project tracker last month. Most people "
            "like it. It is easier to see who is working on what, and the weekly "
            "summary saves time in meetings. There were some problems at the "
            "start, mainly with permissions, but those were fixed quickly. "
            "Overall the change has been positive, although a few people still "
            "prefer the old spreadsheet.",

            # The four below were written by Claude in one draft each and added
            # without scoring them first. Their scores are whatever run_eval
            # shows.

            # AI: an ordinary chatbot answer.
            "Cloud computing has transformed the way businesses store and manage "
            "data. Instead of relying on physical servers, companies can access "
            "computing resources over the internet on a pay-as-you-go basis. This "
            "approach offers several key advantages. First, it reduces upfront "
            "costs, since organizations no longer need to invest in expensive "
            "hardware. Second, it provides scalability, allowing businesses to "
            "increase or decrease resources based on demand. Third, cloud "
            "platforms often include built-in security features and automatic "
            "updates. However, it is important to consider potential challenges, "
            "such as data privacy concerns and dependence on internet "
            "connectivity. Overall, cloud computing offers a flexible and "
            "cost-effective solution for modern organizations.",

            # AI: an ordinary chatbot answer.
            "Maintaining a healthy work-life balance is essential for long-term "
            "well-being and productivity. When work demands begin to take over "
            "personal time, individuals may experience burnout, stress, and "
            "reduced job satisfaction. To create a better balance, it can be "
            "helpful to set clear boundaries, such as defining specific working "
            "hours and avoiding checking emails after a certain time. Taking "
            "regular breaks throughout the day can also help maintain focus and "
            "energy. Additionally, making time for hobbies, exercise, and "
            "relationships contributes to overall happiness. By prioritizing "
            "both professional and personal needs, individuals can lead more "
            "fulfilling and sustainable lives.",

            # Borderline: a neutral notice, the kind a person writes from a
            # template.
            "The community garden will be closed this Saturday for maintenance. "
            "Volunteers are welcome to help with weeding and repairing the "
            "raised beds from 9 a.m. to noon. Please bring your own gloves if "
            "you have them, although we will have a few spare pairs. Water and "
            "snacks will be provided. If you are unable to attend but would "
            "like to contribute, donations of seeds or small tools can be left "
            "in the shed by the main gate. Thank you to everyone who has helped "
            "keep the garden going this year.",

            # Borderline: a short review mixing a personal voice with
            # review-site phrasing.
            "I bought this blender after my old one finally gave up, and so far "
            "I'm pretty happy with it. It handles frozen fruit well and is much "
            "quieter than I expected. The jug is easy to clean, which matters a "
            "lot to me since I use it almost every morning. My only complaint "
            "is that the lid can be a bit stiff to remove. Overall, it offers "
            "good value for the price and I would recommend it to anyone "
            "looking for a reliable everyday blender.",

            # Human: my own writing, chosen because I wrote it, before
            # seeing its score. A personal note about a decision I'm weighing.
            "I feel like I’m cheating in here. My visa doesn’t allow me to have a"
            " business of my own. I have two options.\n"
            "1.\u2060 \u2060Get a job now and continue on my work visa, this would ensure I"
            " cannot have a business legally for now and wait for my husband to "
            "apply and get his greencard kicked in, which might take an year or "
            "so once approved. Then, I can be free to do it.\n"
            "2.\u2060 \u2060\u2060Wait and not get a job as of now and convert to dependent visa"
            " with work authorization by October. Then I can start my own work. "
            "But that means I cannot make any money until October.\n"
            "\n"
            "Because of this, I don’t want to apply for a job, so I can get a "
            "chance in October. My husband is stressed about finances, and I feel"
            " I’m cheating by not trying with my 100%. \n"
            "Again, I’m afraid I’m just making palaces in the clouds. I don’t "
            "know if this would work. It might cause a lot of financial strain on"
            " my husband. I haven’t even planned it all out. So I just feel like "
            "I’m lying and cheating here somewhere and escaping from really being"
            " a financial support to him.",

            # Human: my own writing. Me explaining a project at work, as I'd say it.
            "So the first version of Astech Insights used Flan-T5, and that used "
            "fine-tuning, but then the cost of fine-tuning was on us, and then we"
            " had the GPUs in production, which were costing us some money, and "
            "so forth and so on. So then we found out, then Bedrock was launched,"
            " and realized we could pay for each call rather than keeping a GPU "
            "there. \n"
            "\n"
            "Hence, we figured we can use a better model, which will still not be"
            " training, which will save us some cost, and paying for each call is"
            " cheaper than having our own GPU resources, because, to be honest, "
            "there are not a lot of calls every time. So yeah, that's what we "
            "did. We moved to Anthropic Cloud on Bedrock as asTech Insights II, "
            "and now we are looking at other aspects of using agentic AI where we"
            " could launch the required calibrations automatically.\n",
        ],
    },
    # A bad-input criterion looks like this. Uncomment and adjust if that's one
    # of your five — these are raw request bodies, sent exactly as written.
    #
    {
        "name": "bad input",
        "criterion": 5,
        # The six malformed requests criteria.md names, in the same order.
        "bodies": [
            {"text": "", "creator_id": "eval_bad_empty"},
            {"text": "   \n\t  ", "creator_id": "eval_bad_whitespace"},
            {"creator_id": "eval_bad_missing"},          # no text field at all
            {"text": None, "creator_id": "eval_bad_null"},
            {"text": 12345, "creator_id": "eval_bad_number"},
            {"text": "word " * 50000, "creator_id": "eval_bad_huge"},
        ],
        # Makes run_eval.py check POST /ping still answers afterwards.
        "then_ping": True,
    },
    {
        "name": "appeal path",
        "criterion": 4,
        # Tested by extending run_eval.py (run_appeals), not by hand. Each text
        # is submitted, its content_id appealed, and GET /content/<id> (built
        # from the audit log) read before and after: the appeal must answer 200
        # "under_review", be recorded exactly once, and leave the original
        # decision unchanged. Then one appeal on a made-up content_id, which
        # must get a 404. The texts are filled in below the list: pieces 6–10
        # of "my own writing".
        "appeals": [],
        "reasoning": "I wrote this myself. Please have a person look at it.",
    },
]

# Reuse my own writing rather than pasting it twice.
_by_name = {scenario["name"]: scenario for scenario in SCENARIOS}
_by_name["spread: human group"]["texts"] = _by_name["my own writing"]["texts"][:5]
_by_name["appeal path"]["appeals"] = _by_name["my own writing"]["texts"][5:10]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if "appeals" in scenario:
            if not scenario["appeals"]:
                problems.append(f"scenario {i} has an empty appeals list")
            if not str(scenario.get("reasoning", "")).strip():
                problems.append(f"scenario {i} needs a `reasoning` to appeal with")
            continue

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
