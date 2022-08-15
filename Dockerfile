FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y git ruby ruby-dev build-essential patch zlib1g-dev liblzma-dev nodejs
RUN gem install jekyll bundler
RUN gem install rake

COPY Rakefile* /tmp/
WORKDIR /tmp
RUN rake --tasks

WORKDIR /site

EXPOSE 4000

#CMD ["bundle", "exec", "jekyll", "serve", "-H", "0.0.0.0", "-P", "4000"]
CMD ["jekyll", "serve", "-H", "0.0.0.0", "-P", "4000"]