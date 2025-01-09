# supernote-templates

This repository includes a number of templates designed for eInk devices,
primarily the Supernote A6X2 (Nomad).

These templates are generated from Python to make it easier to experiment with
different layouts and grid sizes.

## Downloading

All generated files are uploaded to the [releases
page](https://github.com/belak/supernote-templates/releases).

## Templates

I tend to write with the toolbars disabled, so these templates

### 4mm Dot Grid

This is very similar to the stock grid templates, but using larger dots. I
personally like being able to see the dots, and making them larger seemed to be
the best way.

### Day Free

Inspired by the Hobonichi Day Free pages - it's essentially a dashed grid with a
solid vertical line. This is a very flexible layout which can be used in many
different ways.

### Daily Planner

Inspired by daily pages in Hobonichi planners, this is very similar to the Day
Free layout with some additional features - there is a date in the upper left
and a mini task list in the upper right. This is a flexible layout which lets
you build your own workflow.

## Building

The build environment for this can be automatically set up if you're using Nix.

If you are not using Nix, you need the following:

- GNU Make
- Python 3
- Poetry
- Inkscape
- (Optional) Reflex

```
# Build all templates
$ make all

# Start a watcher which will automatically build templates when changed (requires reflex)
$ make watch
```

## Contributing

If you have ideas for new template designs, feel free to file an issue or submit
a pull request. I can't promise everything will be accepted, but I'm happy to
consider most ideas.

## License

These templates and the builder are released under the MIT license. You are
welcome to include them in packages of templates, modify them to your needs, and
even sell your own templates based on them. However, you must include the
original LICENSE file along with any distribution of files based on this repo.

Note that you are not required to submit your changes or improvements to this
repo, but you are encouraged to do so if you are willing.
