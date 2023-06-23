# **_Showtime_**

## Date: 6/15/2023

### Authors: [Cody Garcia](https://github.com/popgoesthecultureshock), [Austin Showen](https://github.com/austin-showen), [Jacquelyn Waller](https://github.com/Mwaller129)

### [Trello Board](https://trello.com/b/yoiRt2Xh/showtime)

---

### **_Description_**

**A full-stack Django application allowing users to view, favorite, and review current Broadway shows.**

---

### **_Technologies_**

- Django
- PostgreSQL
- Python
- JavaScript
- HTML
- CSS

---

### **_About the App_**

#### Showtime is a Django web application designed as a central resource to help users track currently running Broadway shows, and the best ways to get tickets for them. Once authenticated, users can review shows that they have seen and favorite shows that they want to attend. Users may also view details on Broadway venues, including a list of all shows currently playing at each venue.

#### Specifications (MVP):

- The home page provides the option to log in via Django authentication, as users need to have an account to access the database.
- Once authenticated, users can view an index of all currently running Broadway shows.
- Authenticated users can also view an index of Broadway theater venues and their locations.
- The site is designed to be reminiscent of the playbill one recieves at any show they'd attend. Navigate through the features of the site by selecting a link at the top, hidden by the eight letters of 'showtime'.
- The detail page for each show lists basic details (title, location, box office hours) as well as buttons to add this title to your 'Seen List' or your 'Wish List' page. There is additionally a section to upload the playbill pic you took, or any other pics oyu'd like to upload on this show page to commemorate your evening.
- Don't know the best or cheapest way to go about seeing the show you want to see? Scroll on the show details page to find out if the show does student or general rush, participates in a lottery, or has leftover standing room tickets.
- Add a review for the show at the bottom of the show details page by clicking the link you find down there, or by selecting the 'Add a Review' section in the Nav Bar.
- Learn more about the developers by going to the aptly named link in the nav bar. Each developer has their personal and professional sites connected.

---

### **_Entity Relationship Diagram_**

#### ![Showtime ERD](/assets/Showtime%20ERD.png)

---

### **_Wireframes_**

#### ![A wireframe of the homepage](/assets/showtime_home.jpeg)

#### The Showtime homepage

#### ![A wireframe of the user's show list](/assets/user_show_list.jpeg)

#### The user's list of shows

#### ![A wireframe of the user's add review page](/assets/user_show_seen.jpeg)

#### The form to add a review of a show

#### ![A wireframe of the user's add show to wishlist page](/assets/user_show_desire.jpeg)

#### The form to add a show to a user's wishlist

---

### Screenshots

![Image]()

![Image]()

![Image]()

### **_Stretch Goals (Post-MVP)_**

- [x] The venue details page connects to an API to show the location of the venue on a map.
- [ ] On the show index page, users can search for a show by title.
- [ ] On the venue index page, users can search for a venue by name.
- [ ] On the show index page, shows that are no longer running are displayed at the bottom of the list and marked as inactive.
- [ ] The show index and venue index pages are limited to a certain number of entries on the first page, with additional pages added as necessary.

---

### **_Credits_**

[playbill.com](https://playbill.com/)
