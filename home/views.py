from django.http import HttpResponse
from django.template import loader
from django.template.context import RequestContext


def home(request):
    # articles = Article.objects.filter(is_active=True).order_by('-last_modified')[:3]
    # content = ContentBox.objects.filter(is_active=True).order_by('-date_created')
    # news = News.objects.filter(is_active=True).order_by('-posted_date')[:5]
    # slides = Slide.objects.filter(is_active=True).order_by('order')
    patti_bio = "Patti is the Owner/Director at Just For You Children’s Centre. She has been a Certified Early" \
                " Childhood Educator since 1999 and a member of the Early Childhood Development Association. " \
                "In 2013, Patti was the recipient of the MacLauchlan Prize for Effective Writing with Excellence " \
                "Award through the University of Prince Edward Island, for her Professional Portfolio submission. " \
                "Patti graduated from UPEI in 2014, with a Bachelor of Child and Family Studies Degree. Working at" \
                " the centre full-time and keeping up with their three children, Patti and her husband Duane have a" \
                " very busy but fulfilling life together. When not enjoying the company of friends and family, you " \
                "can find Patti at any rink in the winter months or out on the soccer fields in the Charlottetown area."

    karen_bio = "Karen has worked in the childcare field for over 25 years. She realized that this was the right fit " \
                "for her after she and her husband welcomed their three children. Karen has her Bachelor of Recreation " \
                "Degree but decided in 2010, to return to school at Holland College to obtain her certificate for" \
                " Early Childhood Care and Education, she completed the program in 2016. Karen works in our Infant " \
                "Room here at Just For You and is a proud Early Childhood Development Association Member.  Karen and " \
                "her husband now are enjoying life with their grown children."

    lisa_bio = "Lisa MacLaren has been employed at Just For You Children’s Centre since 2006 and is an educator with" \
               " the Junior Kindergarten group.  She  graduated from Holland College’s Early Childhood Care and " \
               "Education program in 1991 and is a member of the ECDA.  She was the recipient of the Educating with" \
               " Excellence Award in 2011 and has regularly attended conferences and workshops for professional" \
               " development.  She and her husband Joe reside in Brackley with their two teenaged boys she enjoys" \
               " singing, reading and the outdoors."

    emily_bio = "Emily graduated from Holland College with her diploma in Early Childhood Care and Education in 2016," \
                "and then began working with the 2 & 3 year olds at Just For You shortly after. In the past she has " \
                "been an active member in 4H and enjoys helping at her church. She also likes spending her time with " \
                "friends and family, baking and helping on her family’s dairy farm."

    kathy_bio = "Kathy has been an employee at Just For You Children’s Centre since 2012, working as our experienced" \
                " cook and cleaning staff. She received a recognition award in 2015 for her Commitment To Cooking For" \
                " Quality by the Early Childhood Development Association. She attends workshops within the Healthy" \
                " Eating Alliance to maintain our very delicious and homemade menu. Kathy is a huge part to our " \
                "success at the centre. When not working here full time, Kathy and her husband Leigh, of 40 years " \
                "enjoy spending time with their 5 children and 10 grandchildren."

    crystal_bio = "New Bio coming soon"

    leaanne_bio = "Leanne has been employed here at Just For You, since 2011. She works with the children in the 2yr" \
                  " and 3yr old group.  She moved to Montague, PEI from Ontario with her husband Dave and their two" \
                  " boys Ben and Matthew.  Leanne is an Early Childhood Development Association Member and enjoys " \
                  "reading, travelling and spending time with family and friends."

    marie_bio = "Marie has been employed at Just For You since 2007, where she began as our part time closing staff " \
                "member. She was then hired in 2010, to be our Infant Room Educator, she is also a Early Childhood" \
                " Development Association Member.  Marie has been certified with the entry level from Holland College" \
                "for the Infant/Toddlers in 2014. Marie and her husband Bob live in Charlottetown and enjoy spending" \
                " time with their two grown children. Whenever possible, Marie heads out to her summer cottage, where" \
                " she likes creating  art and crafts, as well as going on nature walks. "

    wendy_bio = "New Bio coming soon"


    # Staff
    staff = [{'name': 'Patti Larkin', 'desc': patti_bio, 'img': 'new_staff_pics/patti_larkin.jpg', 'id': 1},
             {'name': 'Karen Fraser', 'desc': karen_bio, 'img': 'new_staff_pics/karen_fraser.jpg', 'id': 2},
             {'name': 'Lisa MacLaren', 'desc': lisa_bio, 'img': 'new_staff_pics/lisa_maclaren.jpg', 'id': 3},
             {'name': 'Emily Weeks', 'desc': emily_bio, 'img': 'new_staff_pics/emily_weeks_square.jpg', 'id': 4},
             {'name': 'Kathy Campbell', 'desc': kathy_bio, 'img': 'new_staff_pics/kathy_campbell_daugter.jpg', 'id': 5},

             {'name': 'Crystal Affleck', 'desc': crystal_bio, 'img': 'crystal-affleck-square.jpg', 'id': 6},
             {'name': 'Leaanne Gallant', 'desc': leaanne_bio, 'img': 'leaanne-gallant-square.jpg', 'id': 7},
             {'name': 'Marie Hennbery', 'desc': marie_bio, 'img': 'marie-hennebery-square.jpg', 'id': 8},
             {'name': 'Wendy Miller', 'desc': wendy_bio, 'img': 'wendy-miller-square.jpg', 'id': 9},
             # {'name': 'Lisa MacLaren', 'desc': lisa_bio, 'img': 'new_staff_pics/lisa_maclaren.jpg', 'id': 10},

            ]

    t = loader.get_template('index.html')
    c = RequestContext(request, {
        'staff': staff,
    })

    return HttpResponse(t.render(c))



def faq(request):

    t = loader.get_template('home/faq.html')
    c = RequestContext(request, {

    })
    return HttpResponse(t.render(c))


def image_gallery(request):
    image_links = [{'link': '/images'},
                   {'link': 'Patti Larkin'},
                   {'link': 'Patti Larkin'},
                   {'link': 'Patti Larkin'},
                   {'link': 'Patti Larkin'}
                ]

    t = loader.get_template('home/image_gallery.html')
    c = RequestContext(request, {
            'image_links': image_links,
    })
    return HttpResponse(t.render(c))


# def help(request):
#
#     t = loader.get_template('help.html')
#     c = RequestContext(request, {
#
#     })
#     return HttpResponse(t.render(c))