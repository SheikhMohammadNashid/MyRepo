# 1. Use official Apache image
FROM httpd:2.4

# 2. Install git inside the container
RUN apt-get update && apt-get install -y git && apt-get clean

# 3. Set working directory to /website
WORKDIR /website

# 4. Git repo URL (change during build if needed)
ARG REPO_URL=https://github.com/SheikhMohammadNashid/Website.git

# 5. Clone the website repo into /website
RUN git clone $REPO_URL .

# 6. Copy website files from /website to Apache's root folder
RUN rm -rf /usr/local/apache2/htdocs/* \
    && cp -r /website/. /usr/local/apache2/htdocs/


# 7. Expose Apache port
EXPOSE 80


